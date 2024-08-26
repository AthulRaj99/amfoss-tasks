#include <stdio.h>

int main() {
    FILE *f = fopen("input.txt", "r");
    int n;
    fscanf(f, "%d", &n);
    fclose(f);

    f = fopen("output.txt", "w");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n-i-1; j++) fprintf(f, " ");
        for (int j = 0; j < 2*i+1; j++) fprintf(f, "*");
        fprintf(f, "\n");
    }
    for (int i = n-2; i >= 0; i--) {
        for (int j = 0; j < n-i-1; j++) fprintf(f, " ");
        for (int j = 0; j < 2*i+1; j++) fprintf(f, "*");
        fprintf(f, "\n");
    }
    fclose(f);
    return 0;
}

