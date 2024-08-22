#include <fstream> // This includes the file input/output library

int main() {
    // Open the file "input.txt" for reading
    std::ifstream infile("input.txt");
    // Open the file "output.txt" for writing
    std::ofstream outfile("output.txt");

    char c; // A variable to store each character

    // Read each character from the input file and write it to the output file
    while (infile.get(c)) {
        outfile.put(c);
    }

    // Close the files
    infile.close();
    outfile.close();
    return 0;
}

