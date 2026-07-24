#include <stdio.h>

int multi(int a, int b) {
int sum;
sum = a*b;
return sum;
}

int main() {
int a, b;
scanf("%d", &a);
scanf("%d", &b);

printf("%d * %d = %d\n", a, b, multi(a, b));
return 0;

}
