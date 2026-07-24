#include <stdio.h>

int main() {

int age;
printf("quel age as-tu ?\n");
scanf("%d", &age);
printf("Tu as %d ans\n", age);

float money;
printf("combien d'argent possèdes-tu ?\n");
scanf("%f", &money);
printf("Tu as %.2f euros\n", money);

return 0;
}
