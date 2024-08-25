# Read the number from input.txt
with open("input.txt", "r") as file:
    n = int(file.read())

# Write the diamond pattern to output.txt
with open("output.txt", "w") as file:
    # Top half of the diamond
    for i in range(n):
        file.write(" " * (n - i - 1) + "*" * (2 * i + 1) + "\n")
    
    # Bottom half of the diamond
    for i in range(n-2, -1, -1):
        file.write(" " * (n - i - 1) + "*" * (2 * i + 1) + "\n")

