# Microblog

Microblog is a Flask-based blogging application developed through Miguel Grinberg’s Flask tutorial series. It features user authentication, post creation, and a following system.

This project is based on the original repository by Miguel Grinberg, which can be found [here](https://github.com/miguelgrinberg/microblog).

## Features
- User registration, login, and password reset.
- Create, edit, and delete blog posts.
- Follow other users and view their posts.

## Getting Started

### Prerequisites
- Python 3.8+
- Flask
- Virtual Environment

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/miguelgrinberg/microblog
   cd microblog

2. Create and activate virtual environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Set up the database:
   ```bash
   flask db upgrade

5. Run the application
   ```bash
   flask run