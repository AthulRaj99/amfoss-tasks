import java.nio.file.*;

public class Main {
    public static void main(String[] args) throws Exception {
        String data = Files.readString(Path.of("input.txt"));
        Files.writeString(Path.of("output.txt"), data);
    }
}

