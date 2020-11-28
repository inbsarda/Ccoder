
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLESIZE 1

struct BTNode
{
  char *address;
  int TypeID;
  char *data;
  struct BTNode *next;
};

struct ht_t
{
    struct BTNode **nodes;
};

struct ht_t* ht_create()
{
    struct ht_t* ht = (struct ht_t*) malloc(sizeof(struct ht_t));
    ht->nodes = malloc(sizeof(struct BTNode *) * TABLESIZE);
    int i = 0;
    
    for(i = 0; i < TABLESIZE; i++)
    {
        ht->nodes[i] = NULL;
    }
    
    return ht;
}

int hash(char *key)
{
    int val = 0;
    int i = 0;
    int key_len = strlen(key);
    
    for(i = 0; i< key_len; i++)
    {
        val = val * 37 + key[i];
    }
    
    val = val %  TABLESIZE;
    
    return val;
       
}

struct BTNode* BT_Pair(char *address, int TypeID, char *data)
{
   // printf("size %d", sizeof(struct BTNode));
    struct BTNode *node = (struct BTNode*)malloc(sizeof(struct BTNode));
    node->address = (char*)malloc(strlen(address)+1);
    strcpy(node->address, address);
    node->data = (char*)malloc(strlen(data)+1);
    strcpy(node->data, data);
    node->TypeID = TypeID;
    node->next = NULL;
    
    return node;
}

int BTSetData(struct ht_t *ht, char *address, int TypeID, char *data)
{
    int slot = hash(address);
    
    struct BTNode *node = ht->nodes[slot];
    
    if(node == NULL)
    {
        ht->nodes[slot] = BT_Pair(address, TypeID, data);
        return 1;
    }
    
    struct BTNode *prev = NULL; 
    
    while(node != NULL)
    {
        if(strcmp(node->address, address) == 0)
        {
            node->TypeID = TypeID;
            free(node->data);
            node->data = malloc(sizeof(strlen(data) +1));
            strcpy(node->data, data);
            return 1;
        }
        prev = node;
        node = node->next;
    }
    
    prev->next = BT_Pair(address, TypeID, data);
    return 1;
}

char* BTgetData(struct ht_t *ht, char *address, int TypeID)
{
    int slot = hash(address);
    
    struct BTNode *node = ht->nodes[slot];
    
    if(node == NULL)
    {
        return NULL;
    }
    
    while(node != NULL)
    {
         if(strcmp(node->address, address) == 0)
         {
             if(node->TypeID == TypeID)
             {
                  return node->data;
             }
         }
         node = node->next;
    }
        
    return NULL;
}

int main()
{
    struct ht_t *ht = ht_create();  
    
    BTSetData(ht, "AABBCCDDEE", 1, "-50");
    BTSetData(ht, "AABBCCDDGG", 1, "-49");
    BTSetData(ht, "AABBCCDDHH", 1, "-26");
    
    printf("%s", BTgetData(ht, "AABBCCDDGG", 1));

    return 0;
}
