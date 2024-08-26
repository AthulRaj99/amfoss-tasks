#include <iostream>  // For input and output

int main() {
    int n;
    std::cout << "Enter a number: ";
    std::cin >> n;

    // First half of the diamond (including the middle line)
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {  // Print leading spaces
            std::cout << " ";
        }
        for (int j = 0; j < 2 * i + 1; j++) {  // Print stars
            std::cout << "*";
        }
        std::cout << std::endl;  // Move to the next line
    }

    // Second half of the diamond
    for (int i = n - 2; i >= 0; i--) {
        for (int j = 0; j < n - i - 1; j++) {  // Print leading spaces
            std::cout << " ";
        }
        for (int j = 0; j < 2 * i + 1; j++) {  // Print stars
            std::cout << "*";
        }
        std::cout << std::endl;  // Move to the next line
    }

    return 0;  // Indicates successful completion
}

