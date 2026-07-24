#include <stdio.h>

int main() {
	int a = 10;
	int b = 3;
	int fois = a*b;
	int sum = a+b;
	int sous = a-b;
	int div = a/b;
	int divi = a%b;
	printf("%d + %d = %d\n%d + %d = %d\n%d + %d = %d\n%d + %d = %d\n%d + %d = %d\n", a, b, fois, a, b, sum, a, b, sous, a, b, div, a, b, divi);
	return 0;
}
