###################################################
#
# Linked List
#
###################################################

class node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertAtBegining(head,data):
    '''
    Insert node at begining
    '''
    newnode = node(data)
    newnode.next = head
    return newnode

def insertAtEnd(head, newnode):
    '''
    Insert node at the end
    '''
    if head is None:
        head = newnode
        return
    
    while head.next != None:
        head = head.next
    head.next = newnode

def insertInBetween(middlenode, newnode):
    '''
    Insert node in between of the list
    '''
    if middlenode is None:
        print("Node is absent")
        return
    newnode.next = middlenode.next
    middlenode.next = newnode

def deleteNode(head, data):
    '''
    Remove the node from linked list
    '''
    if head.data == data:
        Head = head
        head = head.next
        Head = None
        return

    while head.data != data:
        prev = head
        head = head.next
        if head is None:
            break

    if head is None:
        print("node not found")
        return
    else:
        prev.next = head.next
        head = None

    
def findMiddle(head):
    '''
    Find middle of the linked list
    '''
    node1 = node2 = head

    if head is None:
        print("Empty list")
        
    while node2 is not None and node2.next is not None:
        node1 = node1.next
        node2 = node2.next.next
    return node1

    
def printList(head):
    '''
    Trverse and print the list
    '''
    while head != None:
        print(head.data)
        head = head.next
    


head = node("mon")
e1 = node("Tue")
e2 = node("wed")

head.next = e1
e1.next = e2

e3 = node("thu")
insertAtEnd(head, e3)

e4 = node("fri")
insertInBetween(head.next, e4)

head = insertAtBegining(head, "sun")
deleteNode(head, "fri")
deleteNode(head, "sun")
printList(head)

middle = findMiddle(head)
print(middle.data)
        
