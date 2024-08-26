#include <stdio.h>

int main() {
    int n;

    printf("Enter the number of rows: ");
    scanf("%d", &n);

    // First half of the diamond
    for (int i = 0; i < n; i++) {
        // Loop to print spaces
        for (int j = 0; j < n - i - 1; j++) {
            printf(" ");
        }
        // Loop to print asterisks
        for (int j = 0; j < 2 * i + 1; j++) {
            printf("*");
        }
        printf("\n"); // Move to the next line
    }

    // Second half of the diamond
    for (int i = n - 2; i >= 0; i--) {
        // Loop to print spaces
        for (int j = 0; j < n - i - 1; j++) {
            printf(" ");
        }
        // Loop to print asterisks
        for (int j = 0; j < 2 * i + 1; j++) {
            printf("*");
        }
        printf("\n"); // Move to the next line
    }

    return 0;
}

