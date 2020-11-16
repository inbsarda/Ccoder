/******************************************************************************

                          Binary Tree

*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *left;
    struct node *right;
};

void print_preorder(struct node* root)
{
    if(root != NULL)
    {
        printf("\n %d", root->data);
        print_preorder(root->left);
        print_preorder(root->right);
        
    }
}

void deleteTree(struct node* root)
{
    if(root != NULL)
    {
        printf("\n %d", root->data);
        deleteTree(root->left);
        deleteTree(root->right);
        free(root);
        
    }
    
}

void insertNode(struct node **node, int data)
{
    if(*node == NULL)
    {
        struct node *temp = (struct node *) malloc(sizeof(struct node));
        temp->data = data;
        temp->left = NULL;
        temp->right = NULL;
        *node = temp;
        return;
    }
    
    if(data < (*node)->data)
    {
        insertNode(&(*node)->left, data);
    }
    else
    {
        insertNode(&(*node)->right, data);
    }
}

struct node* search(struct node* root, int data)
{
    if(root == NULL)
    {
        return NULL;
    }
    
    if(root->data == data)
    {
        return root;
    }
    
    if(data < root->data)
    {
        return search(root->left, data);
    }
    else
    {
        return search(root->right, data);
    }
    
    
}

int main()
{
    struct node *root = NULL;
    
    insertNode(&root, 9);
    insertNode(&root, 8);
    insertNode(&root, 7);
    insertNode(&root, 10);
    
    print_preorder(root);   
    
    struct node* temp = search(root, 5);
    
    if(temp)
    {
        printf("\n node found %d", temp->data);
    }
    else
    {
        printf("\n Not found");
    }
    
    deleteTree(root);

    return 0;
}
