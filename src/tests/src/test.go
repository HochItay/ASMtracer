package main

import "fmt"

func iterative_pow(a, b int) int {
	var result int;
	result = 1
 
	for i := 0; i < b; i++ {
		result *= a
	}
	return result 
}

func recursive_pow(a, b int) int {
	
	if (b == 0) {
		return 1
	}
	
	return recursive_pow(a, b-1) * a
}

func main() {
	var a int;
	var b int;
	var iterative_pow_res int;
	var recursive_pow_res int;

	a = 2
	b = 6

	iterative_pow_res = iterative_pow(a, b)
	recursive_pow_res = recursive_pow(a, b)

   /* This is my first sample program. */
   fmt.Printf("the result of %d to the power of %d using iterative_pow is %d\n", a, b, iterative_pow_res)
   fmt.Printf("the result of %d to the power of %d using recursive_pow is %d\n", a, b, recursive_pow_res)
}