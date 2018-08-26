#include<stdio.h>

void insertionsort(int arr[], int size)
{
	int i, j, key;

	for(i = 0; i < size; i++)
	{
		j = i-1;
		key = arr[i];

		while(j >= 0 && (arr[j] > key))
		{
			arr[j+1] = arr[j];
			j = j-1;
		}
		arr[j+1] = key;
	}
}
	



int main()
{
	int a[] = {7, 3, 9, 1, 0, 4};
	int n = sizeof(a)/sizeof(a[0]);
	insertionsort(a, n);

	for(int i = 0; i < n ; i++)
	{
		printf("%d ", a[i]);
	}

	return 0;
}
