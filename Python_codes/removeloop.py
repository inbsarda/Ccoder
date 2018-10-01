##############################################
#
#Find loop in linked list
#
##############################################
class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list():
    def __init__(self):
        self.head = None

    def insert(self, data):
        ptr = node(data)
        ptr.next = None

        if self.head is None:
            self.head = ptr
        else:
            ptr.next = self.head
            self.head = ptr

    def print_list(self):
        temp = self.head

        if self.head is None:
            print("Empty list")
            return

        while temp is not None:
            print(temp.data)
            temp = temp.next

    def detect_and_remove_loop(self):
        fast = self.head
        slow = self.head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                self.removeloop(slow)

    def removeloop(self, slow):
        ptr1 = self.head
        

        while(1):
            ptr2 = slow
            while ptr2.next != slow and ptr2.next != ptr1:
                print("ptr2")
                ptr2 = ptr2.next
                print(ptr2.data)

            if ptr2.next == ptr1:
                break

            print("ptr1")
            print(ptr1.data)
            ptr1 = ptr1.next

        ptr2.next = None
        



llist = linked_list()
llist.insert(1)
llist.insert(2)
llist.insert(3)
llist.insert(4)
llist.insert(5)

llist.head.next.next.next.next.next = llist.head.next.next
llist.detect_and_remove_loop()
llist.print_list()
        
