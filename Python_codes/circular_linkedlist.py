###########################################################
#
#Circular linked list
#
###########################################################

class node():
    def __init__(self, data):
        self.data = data
        self.next = None


class clinkedlist():
    def __init__(self):
        self.head = None


    def insert(self, data):
        ptr = node(data)
        temp = self.head

        if self.head is None:
            ptr.next = ptr
        else:
            while temp.next != self.head:
                temp = temp.next
            ptr.next = self.head
            temp.next = ptr

        self.head = ptr


    def printlist(self):
        temp = self.head

        if self.head is not None:
            while True:
                print(temp.data)
                temp = temp.next
                if temp == self.head:
                    break





clist = clinkedlist()
clist.insert("sun")
clist.insert("mon")
clist.insert("tue")

clist.printlist()
