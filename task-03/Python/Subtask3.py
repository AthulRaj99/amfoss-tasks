# Ask the user to enter a number
n = int(input("Enter a number: "))

# First half of the diamond
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Second half of the diamond
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

