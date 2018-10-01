class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.back = None

    def Enqueue(self, data):
        ptr = node(data)

        if self.back is None:
            self.back = ptr
            self.front = ptr
            return

        self.back.next = ptr
        self.back = self.back.next

    def Dequeue(self):
        if self.front is None:
            print("Empty list")
            return

        data = self.front.data
        self.front = self.front.next
        return data



q = queue()
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(4)
q.Enqueue(5)
q.Enqueue(6)


print(q.Dequeue())
print(q.Dequeue())
print(q.Dequeue())
print(q.Dequeue())

        
