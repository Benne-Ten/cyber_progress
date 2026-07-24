#include <stdio.h>

int main() {

int arr[5] = {3, 7, 2, 9, 1};
int max = arr[0];

for(int i = 0; i < 5; i++) {
if (max < arr[i]) {
max = arr[i];
};
};

printf("le maximum de ce tableau est : %d\n", max);

return 0;
}
