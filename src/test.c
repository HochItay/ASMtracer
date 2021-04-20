#include <stdio.h>


int iterative_pow(int a, int b) {
	int result = 1;
	int i;

	for (i=0; i < b; i++) {
		result *= a;
	}

	return result;
}

int recursive_pow(int a, int b) {
	if (b == 0) {
		return 1;
	}

	return recursive_pow(a, b-1) * a;
}

int main() {
	int a = 2;
	int b = 6;

	int iterative_pow_res = iterative_pow(a, b);
	int recursive_pow_res = recursive_pow(a, b);

	printf("the result of %d to the power of %d using iterative_pow is %d\n", a, b, iterative_pow_res);
	printf("the result of %d to the power of %d using recursive_pow is %d\n", a, b, recursive_pow_res);
	return 0;
}
