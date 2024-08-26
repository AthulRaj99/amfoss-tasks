use std::fs;
use std::io;

fn main() -> io::Result<()> {
    let n: usize = fs::read_to_string("input.txt")?.trim().parse().unwrap();
    let mut diamond = String::new();

    for i in 0..n {
        diamond.push_str(&" ".repeat(n - i - 1));
        diamond.push_str(&"*".repeat(2 * i + 1));
        diamond.push('\n');
    }

    for i in (0..n-1).rev() {
        diamond.push_str(&" ".repeat(n - i - 1));
        diamond.push_str(&"*".repeat(2 * i + 1));
        diamond.push('\n');
    }

    fs::write("output.txt", diamond)?;
    Ok(())
}

