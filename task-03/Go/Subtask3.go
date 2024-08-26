package main

import (
	"fmt"  // # Import the fmt package for input/output
)

func main() {
	var n int
	fmt.Print("Enter a number: ")  // # Ask the user to input a number
	fmt.Scan(&n)  // # Read the user's input and store it in variable n

	// # First half of the diamond (including the middle line)
	for i := 0; i < n; i++ {
		for j := 0; j < n-i-1; j++ {  // # Print leading spaces to center the stars
			fmt.Print(" ")
		}
		for j := 0; j < 2*i+1; j++ {  // # Print the stars for this row
			fmt.Print("*")
		}
		fmt.Println()  // # Move to the next line
	}

	// # Second half of the diamond
	for i := n - 2; i >= 0; i-- {
		for j := 0; j < n-i-1; j++ {  // # Print leading spaces to center the stars
			fmt.Print(" ")
		}
		for j := 0; j < 2*i+1; j++ {  // # Print the stars for this row
			fmt.Print("*")
		}
		fmt.Println()  // # Move to the next line
	}
}

