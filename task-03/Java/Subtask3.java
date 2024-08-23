import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = reader.nextInt();
        
        // Upper part of the diamond
        for (int i = 0; i < n; i++) {
            System.out.println(" ".repeat(n - i - 1) + "*".repeat(2 * i + 1));
        }
        
        // Lower part of the diamond
        for (int i = n - 2; i >= 0; i--) {
            System.out.println(" ".repeat(n - i - 1) + "*".repeat(2 * i + 1));
        }
        
        reader.close();
    }
}

