import java.nio.file.*;

public class Main {
    public static void main(String[] args) {
        // Read the number from input.txt
        String data = Files.readString(Path.of("input.txt")).trim();
        int n = Integer.parseInt(data);

        // Create diamond pattern
        StringBuilder diamond = new StringBuilder();

        // Top half
        for (int i = 0; i < n; i++) {
            diamond.append(" ".repeat(n - i - 1));
            diamond.append("*".repeat(2 * i + 1));
            diamond.append("\n");
        }

        // Bottom half
        for (int i = n - 2; i >= 0; i--) {
            diamond.append(" ".repeat(n - i - 1));
            diamond.append("*".repeat(2 * i + 1));
            diamond.append("\n");
        }

        // Write diamond pattern to output.txt
        Files.writeString(Path.of("output.txt"), diamond.toString());
    }
}

