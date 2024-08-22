use std::fs; // This lets us work with files

fn main() {
    // Read the content of "input.txt" into a variable called "data"
    let data = fs::read_to_string("input.txt").expect("Unable to read file");

    // Write the data into the file "output.txt"
    fs::write("output.txt", data).expect("Unable to write file");
}

