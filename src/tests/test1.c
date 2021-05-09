#include <stdio.h>

int main() {
    printf("hello World!");
    return 0;
}

int isPrime(int n) {
	int i;
	for (i = 2; i < n; ++i) {
		if (n % i == 0) {
			return 0;
		}
	}
	return 1;
}
