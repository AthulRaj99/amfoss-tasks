# Read the number from input.txt
n = File.read!("input.txt") |> String.to_integer()
# Create the diamond pattern as a single string
diamond_pattern = 
  # Top half of the diamond
  for i <- 0..(n-1), into: "" do
    String.duplicate(" ", n - i - 1) <> String.duplicate("*", 2 * i + 1) <> "\n"
  end
  # Bottom half of the diamond
  <> 
  for i <- (n-2)..0, into: "" do
    String.duplicate(" ", n - i - 1) <> String.duplicate("*", 2 * i + 1) <> "\n"
  end

# Write the diamond pattern to output.txt
File.write!("output.txt", diamond_pattern)

