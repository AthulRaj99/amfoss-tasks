package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	data, _ := ioutil.ReadFile("input.txt")  // Read the input file
	n, _ := strconv.Atoi(strings.TrimSpace(string(data)))  // Convert the data to an integer

	var output strings.Builder  // Use a builder to create the output

	// Upper half of the diamond
	for i := 0; i < n; i++ {
		output.WriteString(strings.Repeat(" ", n-i-1))  // Leading spaces
		output.WriteString(strings.Repeat("*", 2*i+1))  // Stars
		output.WriteString("\n")
	}

	// Lower half of the diamond
	for i := n - 2; i >= 0; i-- {
		output.WriteString(strings.Repeat(" ", n-i-1))  // Leading spaces
		output.WriteString(strings.Repeat("*", 2*i+1))  // Stars
		output.WriteString("\n")
	}

	ioutil.WriteFile("output.txt", []byte(output.String()), 0644)  // Write the output to a file
}

