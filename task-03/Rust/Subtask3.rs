use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();

    for i in 0..n {
        println!("{:width$}{}", "", "*".repeat(2 * i + 1), width = n - i - 1);
    }
    for i in (0..n-1).rev() {
        println!("{:width$}{}", "", "*".repeat(2 * i + 1), width = n - i - 1);
    }
}

