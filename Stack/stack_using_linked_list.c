#include<stdio.h>

struct node
{
    int data;
    struct node *next;
};

typedef struct node node;

node *top = NULL;

int main()
{
    push(30);
    push(20);
    push(10);

    while(!IsEmpty())
    {
        printf("\n top %d", pop());
    }

    printf("\n top %d", peak());

    return 0;
}

void push(int data)
{
    node *tmp;
    tmp = malloc(sizeof(node));
    tmp->data = data;
    tmp->next = top;
    top = tmp;
}

int pop()
{
    int val;
    node *tmp;
    tmp = top;
    top = top->next;
    val = tmp->data;
    free(tmp);
    return val;
}

int IsEmpty()
{
    if(top == NULL)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int peak()
{
    if(!IsEmpty())
    {
        return top->data;
    }
    else
    {
        return -1;
    }
}
