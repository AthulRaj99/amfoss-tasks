const fs = require('fs');

// Read the number from input.txt
const n = parseInt(fs.readFileSync('input.txt', 'utf8'));

// Create the diamond pattern
let diamond = '';

// Top half of the diamond
for (let i = 0; i < n; i++) {
    diamond += ' '.repeat(n - i - 1) + '*'.repeat(2 * i + 1) + '\n';
}

// Bottom half of the diamond
for (let i = n - 2; i >= 0; i--) {
    diamond += ' '.repeat(n - i - 1) + '*'.repeat(2 * i + 1) + '\n';
}

// Write the diamond pattern to output.txt
fs.writeFileSync('output.txt', diamond);

