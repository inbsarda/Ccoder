
#include<stdio.h>

#define MAXSIZE 5
int stack[5];
int track_stack[5];
int top = -1;
int track_top = -1;

int main()
{
    push(4);
    push(2);
    push(7);
    push(4);
    push(10);

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
    if(track_top == -1)
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

        if(top == 0)
        {
            track_top = track_top + 1;
            *(track_stack + track_top) = data;
        }

        if(data > *(track_stack + track_top))
        {
            track_top = track_top + 1;
            *(track_stack + track_top) = data;
        }
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
        data = *(track_stack + track_top);
        track_top = track_top - 1;
        top = top - 1;
        return data;
    }
    else
    {
        printf("\n Stack is empty.");
        return 0;
    }
}

