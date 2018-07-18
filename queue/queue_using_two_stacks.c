#include<stdio.h>

#define MAXSIZE 10

int stack1[MAXSIZE];
int stack2[MAXSIZE];
int top1 = -1, top2 = -1;

int main()
{
    int i;
    int data;
    for(i=0; i<10; i++)
    {
        printf("\n Enter data:");
        scanf("%d", &data);
        push(data);
    }

    for(i=0; i<10; i++)
    {
        printf("\n data: %d",pop());
    }

    return 0;
}

void push(data)
{
    top1 = top1 + 1;
    stack1[top1] = data;
}

int pop()
{
    while(top1 != -1)
    {
        top2++;
        stack2[top2] = stack1[top1];
        top1--;
    }
    int val = stack2[top2];

    top2--;
    while(top2 != -1)
    {
        top1++;
        stack1[top1] = stack2[top2];
        top2--;
    }

    return val;
}
