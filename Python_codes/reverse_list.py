##################################################################
#
# Reverse the linked list
#
##################################################################

class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        ptr = node(data)

        if self.head is None:
            self.head = ptr
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = ptr

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def reverselist(self):
        temp = self.head
        prev = None
        fwd = None

        while temp is not None:
            #print(temp.data)
            fwd = temp.next
            temp.next = prev
            prev = temp
            temp = fwd
        self.head = prev




llist = linkedlist()
llist.insert("sun")
llist.insert("mon")
llist.insert("tue")
llist.insert("wed")

llist.printlist()
llist.reverselist()
llist.printlist()
