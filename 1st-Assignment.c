//Write in program in c that  removes duplicates from a Sorted array

#include <stdio.h>

int main()
{
    int i, j = 0, n = 10;
    int arr[10];
    int a[10] = {1,2,2,3,3,4,5,6,7,8};


    arr[j] = a[0];  // The first element will be 1st
    j++;


    for (i = 1; i < n; i++)
    {
        if (a[i] != a[i-1])   // Compare with previous
        {
            arr[j] = a[i];
            j++;
        }
    }

    printf("Array after removing duplicates:\n");
    for (i = 0; i < j; i++)
    {
        printf("%d ", arr[i]);
    }

    return 0;
}

