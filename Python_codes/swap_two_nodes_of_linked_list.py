class node:
    def __init__(self,data):
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

        ptr.next = self.head
        self.head = ptr

    def printlist(self):
        if self.head is None:
            print("Empty list");
            return

        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def swapnode(self, x, y):
        if self.head is None:
            print("Empty list");
            return

        if x == y:
            print("Both values are same")
            return

        tempx = self.head
        tempy = self.head
        prevx = None
        prevy = None
        while tempx is not None and tempx.data != x:
            prevx = tempx
            tempx = tempx.next

        while tempy is not None and tempy.data != y:
            prevy = tempy
            tempy = tempy.next
            
        if tempx is None or tempy is None:
            return

        if prevx is not None:
            prevx.next = tempy
        else:
            self.head = tempy

        if prevy is not None:
            prevy.next = tempx
        else:
            self.head = tempx
        

        tempz = tempy.next
        tempy.next = tempx.next
        tempx.next = tempz
            
        
        
        
llist = linkedlist()
llist.insert(1)
llist.insert(2)
llist.insert(3)
llist.insert(4)
llist.insert(5)
llist.insert(6)
llist.insert(7)
llist.insert(8)

llist.printlist()

llist.swapnode(8,1)
print("After swap")
llist.printlist()

