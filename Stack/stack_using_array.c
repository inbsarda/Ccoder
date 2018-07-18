#include<stdio.h>

#define MAXSIZE 5
int stack[5];
int top = -1;

int main()
{
    push(1);
    push(2);
    push(3);
    push(4);
    push(5);

    printf("\n peak of stack %d", peak());

    while(!IsEmpty())
    {
        printf("\n stack top %d", pop());
    }
    return 0;
}

int peak()
{
    return *(stack + top);
}

int IsFull()
{
    if(top == MAXSIZE)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int IsEmpty()
{
    if(top == -1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

void push(int data)
{
    if(!IsFull())
    {
        top = top + 1;
        *(stack + top) = data;
    }
    else
    {
        printf("\n stack is full.");
    }
}

int pop()
{
    int data;
    if(!IsEmpty())
    {
        data = *(stack + top);
        top = top - 1;
        return data;
    }
    else
    {
        printf("\n Stack is empty.");
        return 0;
    }
}

