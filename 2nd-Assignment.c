//Write a Program to find the largest number among three numbers in an array .
#include <stdio.h>
int main()
{
    int n=3,num[]={10,50,30};
    int max = num[0];
    for (int i=1;i<n;i++) // 1st a max er value 10 niye dhukbe compare korbe 50 er sathe
    {
        if (max < num[i])
            max = num[i];
    }
    printf("The Largest number is %d ", max);

}
