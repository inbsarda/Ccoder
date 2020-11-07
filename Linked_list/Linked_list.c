/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>

struct node 
{
    int data;
    struct node* next;
};

struct node* head = NULL;

void printList()
{
    struct node* ptr = head;
    
    printf("\nPrinting list : ");
    
    while(ptr)
    {
        printf("%d ", ptr->data);
        ptr = ptr->next;
    }
    
    printf("\n");
}

void insertNode(int nData)
{
    struct node* temp = (struct node*) malloc(sizeof(struct node));
    temp->data = nData;
    temp->next = NULL;
    
    if(head == NULL)
    {
        head = temp;
    }
    else
    {
        struct node* link = head;
        while(link->next)
        {
            link = link->next;
        }
        
        link->next = temp;
    }
}

struct node* deleteNode(int nData)
{
    struct node *current = head;
    struct node *previous = NULL;
    
    /*List is empty*/
    if(head == NULL)
    {
        return NULL;
    }
    
    while(current->data != nData)
    {
        if(current->next == NULL)
        {
            printf("\n node not found");
            return NULL;
        }
        previous = current;
        current = current->next;
    }
    
    if(current == head)
    {
        head = head->next;
    }
    else
    {
        previous->next = current->next;
    }
    
    return current;
}

void reverseList()
{
    struct node *current = head;
    struct node *previous = NULL;
    struct node *temp = NULL;
    
    while(current != NULL)
    {
        temp = current;
        current = current->next;
        temp->next = previous;
        previous = temp;
    }
    
    head = previous;
}

int lengthList()
{
    struct node *ptr = head;
    int length = 0;
    
    /* List is empty */
    if(head == NULL)
    {
        return 0;
    }
    
    while(ptr)
    {
        length++;
        ptr = ptr->next;
    }
    
    return length;
}

void sortList()
{
    int temp;
    struct node *current = NULL;
    struct node *next =  NULL;
    int i, j, k;
    int size = lengthList();
    
    k = size;
    
    printf("\n %d", k);
    
    for(i = 0; i < (size -1); i++, k--)
    {
        current = head;
        next =  head->next;
        
        //printf("\n %d", k);
        
        for(j = 1; j < k; j++)
        {
            if(current->data > next->data)
            {
                temp = current->data;
                current->data = next->data;
                next->data = temp;
            }
            
            current = current->next;
            next = next->next;
        }
        
    }
}

void removeDuplicate()
{
    struct node* current = head->next;
    struct node* runner = NULL;
    struct node* previous = head;
    
    while(current != NULL)
    {
        runner = head;
        while(current != runner)
        {
            if(current->data == runner->data)
            {
                current = current->next;
                previous->next = current;
                break;
            }
            runner = runner->next;
        }
        
        if(runner == current)
        {
            previous = current;
            current = current->next;
        }
    }
}

int main()
{
    insertNode(1);
    insertNode(2);
    insertNode(1);
    insertNode(4);
    
    printList();
    
    //struct node *dNode = deleteNode(2);
    //printf("\n Deleted node %d", dNode->data);
    removeDuplicate();
    printList();
    
    reverseList();
    printList();
    
    sortList();
    printList();

    return 0;
}
