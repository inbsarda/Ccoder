/** You have two numbers represented by a linked list, where each node contains a single digit. 
The digits are stored in reverse order, such that the 1’s digit is at the head of the list. 
Write a function that adds the two numbers and returns the sum as a linked list.

EXAMPLE
Input: (3 -> 1 -> 5), (5 -> 9 -> 2)
Output: 8 -> 0 -> 8
**/

#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node* next;
};

struct node *head1 = NULL;
struct node *head2 = NULL;

void insertToList1(int value)
{
    struct node* temp = (struct node*) malloc(sizeof(struct node));
    temp->data = value;
    temp->next = NULL;
    
    if(head1 == NULL)
    {
        head1 = temp;
    }
    else
    {
        struct node* ptr = head1;
        while(ptr->next != NULL)
        {
            ptr = ptr->next;
        }
        
        ptr->next = temp;
    }
    
}

void insertToList2(int value)
{
    struct node* temp = (struct node*) malloc(sizeof(struct node));
    temp->data = value;
    temp->next = NULL;
    
    if(head2 == NULL)
    {
        head2 = temp;
    }
    else
    {
        struct node* ptr = head2;
        while(ptr->next != NULL)
        {
            ptr = ptr->next;
        }
        
        ptr->next = temp;
    }
    
}

void printList(struct node **head)
{
    struct node* ptr = *head;
    while(ptr != NULL)
    {
        printf("%d ", ptr->data);
        ptr = ptr->next;
    }
    
    printf("\n");
}

void addList()
{
    struct node* ptr = NULL;
    struct node* tmp = (struct node*) malloc(sizeof(struct node));;
    int addition;
    int carry = 0;
    struct node* ptr1 = head1;
    struct node* ptr2 = head2;
    
    while(ptr1 != NULL && ptr2 != NULL)
    {
        addition = ((ptr1->data + ptr2->data + carry) % 10);
        carry = ((ptr1->data + ptr2->data + carry) / 10);
        tmp->data = addition;
        tmp->next = NULL;
        
         printf("%d ", addition);
        
        if(ptr == NULL)
        {
            ptr = tmp;
        }
        else
        {
            while(ptr->next != NULL)
            {
                ptr = ptr->next;
            }
            
            ptr->next = tmp;
        }
        
        ptr1 = ptr1->next;
        ptr2 = ptr2->next;
    }
    
}


int main()
{
    insertToList1(3);
    insertToList1(1);
    insertToList1(5);
    insertToList1(1);
    
    printList(&head1);
    
    insertToList2(5);
    insertToList2(9);
    insertToList2(2);
    insertToList2(2);
    
    printList(&head2);
    
    addList();

    return 0;
}
