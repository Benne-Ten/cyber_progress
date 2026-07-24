#include <stdio.h>

int main() {

int arr[5];
int sum;

for(int i = 1; i < 6; i++) {
for(int j = 1; j < 6; j++) {
arr[j-1] = i*j;
};
for(int x = 0; x < 5; x++) {
printf("%d ", arr[x]);
};
printf("\n");
};

return 0;
}
