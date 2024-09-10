import click
import os
import requests
from bs4 import BeautifulSoup
from imdb import Cinemagoer

# Function to extract IMDb ID from filename
def extract_imdb_id(filename):
    ia = Cinemagoer()
    movie_name = os.path.splitext(os.path.basename(filename))[0]
    try:
        search_results = ia.search_movie(movie_name)
        if search_results:
            movie = search_results[0]
            imdb_id = f"tt{movie.movieID}"
            print(f"Found IMDb ID: {imdb_id} for movie '{movie['title']}'")
            return imdb_id
        else:
            print("IMDb ID not found.")
            return None
    except Exception as e:
        print(f"Error retrieving IMDb ID: {e}")
        return None

# Function to scrape subtitles from OpenSubtitles
def scrape_subtitles(imdb_id, language_code):
    url = f'https://www.opensubtitles.org/en/search/sublanguageid-{language_code}/imdbid-{imdb_id}'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        subtitles = []
        for item in soup.find_all('a', class_='bnone'):
            name = item.text.strip()
            download_link = item['href']
            subtitles.append({'name': name, 'url': download_link})
        if not subtitles:
            print("No subtitles found.")
        return subtitles
    except requests.RequestException as e:
        print(f"Error fetching subtitles: {e}")
        return []

# Function to download the exact subtitle file
def download_subtitle(subtitle_url, output_folder):
    try:
        # Construct full URL to access subtitle download page
        subtitle_url = "https://www.opensubtitles.org" + subtitle_url
        print(f"Accessing subtitle page: {subtitle_url}")
        subtitle_page = requests.get(subtitle_url)
        subtitle_soup = BeautifulSoup(subtitle_page.content, 'html.parser')

        # Updated selector to find the correct download link
        download_button = subtitle_soup.find('a', {'id': 'bt-dwl-bt'})

        # Debug information to check what we found
        print(f"Download button found: {download_button}")

        if download_button and download_button.has_attr('href'):
            download_link = download_button['href']
            print(f"Extracted download link: {download_link}")

            # Construct the full URL of the subtitle file
            file_url = "https://www.opensubtitles.org" + download_link
            filename = file_url.split("/")[-1]
            filepath = os.path.join(output_folder, filename)

            # Attempt to download the actual subtitle file
            response = requests.get(file_url, allow_redirects=True)
            content_disposition = response.headers.get('content-disposition')
            print(f"Content disposition: {content_disposition}")

            # Check if it's a valid subtitle file and not just another page
            if content_disposition and 'attachment' in content_disposition:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded {filename} to {filepath}")
            else:
                print("Received redirect or webpage instead of a subtitle file.")
        else:
            print("Failed to find the direct download link.")
    except Exception as e:
        print(f"Error downloading subtitle: {e}")

# Function to process a single file
def process_file(file_path, output_folder, language_code):
    imdb_id = extract_imdb_id(file_path)
    if imdb_id:
        subtitles = scrape_subtitles(imdb_id, language_code)
        if subtitles:
            print("Available subtitles:")
            for idx, subtitle in enumerate(subtitles):
                print(f"{idx + 1}: {subtitle['name']}")
            try:
                choice = int(input("Enter the number of the subtitle to download: ")) - 1
                if 0 <= choice < len(subtitles):
                    download_subtitle(subtitles[choice]['url'], output_folder)
                else:
                    print("Invalid choice")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("No subtitles available to choose from.")
    else:
        print("IMDb ID not found.")

# Function to handle batch mode
def handle_batch_mode(directory_path, output_folder, language_code):
    if os.path.isdir(directory_path):
        print("Batch mode enabled. Processing all movies in the directory...")
        for file_name in os.listdir(directory_path):
            if file_name.lower().endswith(('.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.mpeg', '.mpg', '.webm', '.mpeg4')):
                full_path = os.path.join(directory_path, file_name)
                print(f"Processing {file_name}...")
                process_file(full_path, output_folder, language_code)
    else:
        print(f"Directory not found: {directory_path}")

# Main CLI interface
@click.command()
@click.option('-o', '--output', default='.', help='Specify the output folder for subtitles')
@click.option('-b', '--batch-download', is_flag=True, help='Enable batch mode')
@click.option('-l', '--language', default='eng', help='Specify the language code for subtitles (default: eng)')
@click.argument('file_path', required=True)
def main(output, batch_download, language, file_path):
    if batch_download:
        handle_batch_mode(file_path, output, language)
    else:
        process_file(file_path, output, language)

# Ensure the script runs when executed
if __name__ == '__main__':
    main()
