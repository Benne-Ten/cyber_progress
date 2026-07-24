#include <stdio.h>

int main() {
float a, b; char op;
float sum;
scanf("%f", &a);
scanf("%f", &b);
scanf(" %c", &op);

if (op == '+') {
	sum = a + b;
	printf("le résultat est : %.2f\n", sum);
} else if (op == '/' && b>0) {
        sum = a / b;
	printf("le résultat est : %.2f\n", sum);
} else if (op == '-') {
        sum = a - b;
	printf("le résultat est : %.2f\n", sum);
} else if (op == '*') {
        sum = a * b;
	printf("le résultat est : %.2f\n", sum);
} else {
	printf("soit mauvais opérateur soit / avec 0");
};

}
