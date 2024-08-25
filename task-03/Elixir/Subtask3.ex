# Get the number from the user
n = String.to_integer(IO.gets("Enter a number: "))

# Top half of the diamond
for i <- 0..(n-1) do
  IO.puts String.duplicate(" ", n - i - 1) <> String.duplicate("*", 2 * i + 1)
end

# Bottom half of the diamond
for i <- (n-2)..0 do
  IO.puts String.duplicate(" ", n - i - 1) <> String.duplicate("*", 2 * i + 1)
end

