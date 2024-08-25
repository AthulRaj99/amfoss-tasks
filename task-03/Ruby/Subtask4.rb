# Read the number from input.txt
n = File.read("input.txt").to_i

# Write the diamond pattern to output.txt
File.open("output.txt", "w") do |file|
  # Top half of the diamond
  for i in 0...n
    file.puts " " * (n - i - 1) + "*" * (2 * i + 1)
  end

  # Bottom half of the diamond
  for i in (n-2).downto(0)
    file.puts " " * (n - i - 1) + "*" * (2 * i + 1)
  end
end

