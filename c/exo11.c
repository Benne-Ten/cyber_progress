#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool in(char str) {
char voy[6] = {'a', 'e', 'i', 'o', 'u', 'y'};
for (int i =0; i < 6; i++) {
if (voy[i] == str) {
return true;
};
};
return false;
};

int main() {

char str[50];
int nb = 0;

scanf("%s", str);
for(int i = 0; i < strlen(str); i++) {
if (in(str[i]) == true) {
nb += 1;
};
};

printf("cette chaine de char possède %d voyelles\n", nb);

return 0;
}
