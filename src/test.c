#include <stdio.h>
#include <unistd.h>

int isPrime(int n) {
	for (int i = 2; i < n; ++i) {
		if (n % i == 0) {
			return 0;
		}
	}
	return 1;
}

int main() {
	int i = 23;
	isPrime(i);
	printf("hello!");
	return 0;
}
