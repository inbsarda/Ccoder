#include <stdio.h>

int main()
{
    int B[] = {1, 1, 0, 1, 1};
    printf("count %d", solution(B, 5));

    return 0;
}

int solution(int A[], int N)
{
    int i;
    int c1 = 0, c2 = 0;
    int num = 0;
    
    //Compare with sequence 010101....
    for(i=0; i<N; i++)
    {
        if(A[i] != num)
        {
            c1++;
        }
        
        num = !num;
    }
    
    num = 1;
    
    //Compare with sequence 101010.......
    for(i=0; i<N; i++)
    {
        if(A[i] != num)
        {
            c2++;
        }
        
        num = !num;
    }
    
    //Return minimum count
    if(c1 < c2)
    {
        return c1;
    }
    else
    {
        return c2;
    }
}
