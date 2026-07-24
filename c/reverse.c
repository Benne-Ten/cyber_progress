#include <stdio.h>
#include <string.h>

int main() {

char str[50];
char reverse[50];
int j = 0;

scanf("%s", str);
for (int i = strlen(str)-1; i >= 0; i--) {
reverse[j] = str[i];
j += 1;
};

reverse[j] ='\0';
printf("%s\n", reverse);

return 0;
}
