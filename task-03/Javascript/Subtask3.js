// Get the number from the user
const n = parseInt(prompt("Enter a number:"));

// Top half of the diamond
for (let i = 0; i < n; i++) {
  console.log(" ".repeat(n - i - 1) + "*".repeat(2 * i + 1));
}

// Bottom half of the diamond
for (let i = n - 2; i >= 0; i--) {
  console.log(" ".repeat(n - i - 1) + "*".repeat(2 * i + 1));
}

