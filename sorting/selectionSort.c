#include<stdio.h>

void selectionsort(int arr[], int n)
{
    int i, j;
    int min, tmp;

    for(i = 0; i < n; i++)
    {
        min = i;
        for(j = i+1; j < n; j++)
        {
            if(arr[j] < arr[min])
            {
                min = j;
            }
        }
        if( i != min)
        {
            tmp = arr[min];
            arr[min] = arr[i];
            arr[i] = tmp;
        }

    }
}

int main()
{
    int a[] = {8, 6, 4, 1, 9, 0};
    int size = sizeof(a) / sizeof(a[0]);
    int i;
    selectionsort(a, size);
    for(i = 0; i < size; i++)
    {
        printf("%d ", a[i]);
    }

    return 0;
}
