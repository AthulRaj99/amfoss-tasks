package main // This tells the program it's the main package

import (
    "io/ioutil" // This lets us work with files
)

func main() {
    // Read the content of "input.txt" into a variable called "data"
    data, _ := ioutil.ReadFile("input.txt")

    // Write the data into the file "output.txt"
    _ = ioutil.WriteFile("output.txt", data, 0644)
}

