/******************************************************************************
Circular Linked List
*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node* next;
};

struct node *head = NULL;

void insertNodeatLast(int val)
{
    struct node *temp = (struct node*) malloc(sizeof(struct node *));
    temp->data = val;
    temp->next = NULL;
    
    struct node *ptr = NULL;
    
    if(head == NULL)
    {
        head = temp;
        head->next = head;
    }
    else
    {
        ptr = head;
        
        while(ptr->next != head)
        {
            ptr = ptr->next;
        }
    
        temp->next = ptr->next;
        ptr->next = temp;
        
    }
    
}

void printList()
{
    struct node *ptr = head;
    
    if(ptr == NULL)
    {
        printf("\n List is enpty");
    }
    
    printf("\n");
    
    do
    {
        
        printf("%d ", ptr->data);
        ptr = ptr->next;
    }while(ptr != head);
}


struct node* deleteNode(int val)
{
    struct node *ptr = head;
    struct node *ptr2 = NULL;
    
    if(head == NULL)
    {
        printf("\n empty list");
        return NULL;
    }
    
    if((head->next == head) && (head->data != val))
    {
        printf("\n element not found");
        return NULL;
    }
    
    do
    {
        if(ptr->next->data == val)
        {
            ptr2 = ptr->next;
            ptr->next = ptr->next->next;
            if(ptr2 == head)
            {
                head = ptr->next;
            }
            break;
        }
        ptr = ptr->next;
        
    }while(ptr != head);
    
    return ptr2;
    
}

int main()
{
    insertNodeatLast(1);
    insertNodeatLast(2);
    insertNodeatLast(3);
    insertNodeatLast(4);
    
    printList();
    
    struct node *dNode = deleteNode(2);
    
    printList();

    return 0;
}
