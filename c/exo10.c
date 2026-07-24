#include <stdio.h>
#include <string.h>

int main() {

char str[50];
int nb = 0;

scanf("%s", str);
nb = strlen(str);
printf("cette chaine de char possède %d lettres\n", nb);

return 0;
}
