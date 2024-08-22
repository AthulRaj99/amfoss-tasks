const fs = require('fs');

let data = fs.readFileSync('input.txt', 'utf8');
fs.writeFileSync('output.txt', data);

