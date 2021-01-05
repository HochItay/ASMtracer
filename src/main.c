int isPrime(int n) {
	for (int i = 2; i < n; ++i) {
		if (n % i == 0) {
			return 0;
		}
	}
	return 1;
}

int main() {
	int i = 0;
	int n = 12;
	i += n;
	isPrime(i);
	return 0;
}
