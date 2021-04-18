int isPrime(int n) {
	for (int i = 2; i < n; ++i) {
		if (n % i == 0) {
			return 0;
		}
	}
	return 1;
}

void recursiveFunc(int n) {
	if (n == 1) return;
	isPrime(n);
	recursiveFunc(n-1);
}

int main() {
	recursiveFunc(5);
	return 0;
}
