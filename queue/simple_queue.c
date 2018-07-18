#include<stdio.h>

#define MAXSIZE 5
int q[MAXSIZE];

int main()
{
    int front, rear, data;
    init(&front, &rear);

    while(!IsFull(rear))
    {
        printf("\n Enter new element : ");
        scanf("%d", &data);
        enqueue(&rear, data);
    }

    while(!empty(&front, &rear))
    {
        printf("\n ele : %d %d %d", dequeue(&front), front, rear);
    }

    return 0;
}

void init(int *head, int *tail)
{
    *head = *tail = 0;
}

int empty(int *head, int *tail)
{
    return *head == *tail;
}

void enqueue(int *tail, int data)
{
    q[(*tail)++] = data;
}

int dequeue(int *head)
{
    return q[(*head)++];
}

int IsFull(int tail)
{
    return tail == MAXSIZE;
}
