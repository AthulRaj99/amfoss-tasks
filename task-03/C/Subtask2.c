#include <stdio.h> // This includes the standard input/output library

int main() {
    // Open the file "input.txt" in read mode
    FILE *infile = fopen("input.txt", "r");
    // Open the file "output.txt" in write mode
    FILE *outfile = fopen("output.txt", "w");
    char c; // A variable to store each character

    // Read each character from the input file and write it to the output file
    while ((c = fgetc(infile)) != EOF) {
        fputc(c, outfile);
    }

    // Close the files
    fclose(infile);
    fclose(outfile);
    return 0;
}

