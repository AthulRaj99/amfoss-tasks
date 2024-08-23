#  Ask the user to enter a number
puts "Enter a number:"
n = gets.to_i  

# First half of the diamond
for i in 0...n
  spaces = n - i - 1
  stars = 2 * i + 1
  puts " " * spaces + "*" * stars
end
# Second half of the diamond
for i in (n-2).downto(0)
  spaces = n - i - 1
  stars = 2 * i + 1
  puts " " * spaces + "*" * stars
end
