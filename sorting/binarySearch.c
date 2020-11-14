/******************************************************************************
	Binary Search

*******************************************************************************/

#include <stdio.h>

int binarySearch(int arr[7], int start, int end, int x)
{
    if(end >= start)
    {
        
        int mid = start + ((end - start) / 2);
    
        if(arr[mid] == x)
        {
            return mid;
        }
    
        if(arr[mid] < x)
        {
            return binarySearch(arr, start, mid-1, x);
        }
        else
        {
            return binarySearch(arr, mid+1, end, x);
        }
    }
    
    return -1;
}

int main()
{
    int arr1[7] = {7, 6, 5, 4, 3, 2, 1};
    
    printf("%d", binarySearch(arr1, 0, 6, 2));

    return 0;
}
