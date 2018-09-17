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
        if self.head is None:
            print("Empty list")
            return

        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def swap2node(self):
        temp = self.head

        if temp is None:
            return

        while (temp is not None and temp.next is not None):
            temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next.next
        


llist = linkedlist()
llist.insert(1)
llist.insert(2)
llist.insert(3)
llist.insert(4)
llist.insert(5)
llist.insert(6)

#llist.printlist()
llist.swap2node()
llist.printlist()
