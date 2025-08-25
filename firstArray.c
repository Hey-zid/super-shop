#include <stdio.h>

int main() {
    int n, i, j = 0;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    int arr[n], newArr[n];


    printf("Enter %d numbers:\n", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }


    newArr[j++] = arr[0];


    for (i = 1; i < n; i++) {
        if (arr[i] != arr[i + 1]) {
            newArr[j++] = arr[i];
        }
    }


    printf("Array after removing duplicates:\n");
    for (i = 0; i < j; i++) {
        printf("%d ", newArr[i]);
    }
    printf("\n");

    return 0;
}
