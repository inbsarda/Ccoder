#include<stdio.h>

#define MAXSIZE 5
int q[MAXSIZE];

struct node
{
    int data;
    struct node *next;
};

typedef struct node node;

int main()
{
    int i, data;
    node *front = NULL;
    node *rear = NULL;
    //init(front, rear);
    printf("%d %d", front, rear);

    for(i = 0; i<5; i++)
    {
        printf("\n Enter new element : ");
        scanf("%d", &data);
        enqueue(rear, data);
    }

    while(!empty(rear))
    {
        printf("\n ele : %d %d %d", dequeue(&front), front, rear);
    }

    return 0;
}

void init(node *head, node *tail)
{
    head = NULL;
    tail = NULL;
}

int empty(node *tail)
{
    return tail == NULL;
}

void enqueue(node *tail, int data)
{
    node *tmp;
    tmp = malloc(sizeof(node));
    tmp->data = data;
    tmp->next = NULL;
    if(!empty(tail))
    {
        tail->next = tmp;
    }

    tail = tmp;
}

int dequeue(node *head)
{
    node *tmp = head;
    int val = head->data;
    head = head->next;
    free(tmp);
    return val;
}



