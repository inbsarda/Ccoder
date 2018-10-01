class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)
        print(self.items)

    def pop(self):
        return self.items.pop()

class queue:
    def __init__(self):
        self.stack1 = stack()
        self.stack2 = stack()
        

    def Enqueue(self, data):
        self.stack1.push(data)

    def Dequeue(self):
        if self.stack1.isEmpty():
            print("Empty queue")
            return

        while self.stack1.isEmpty() is not True:
            data = self.stack1.pop()
            self.stack2.push(data)

        return self.stack2.pop()


q = queue()
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(4)

print(q.Dequeue())
print(q.Dequeue())
print(q.Dequeue())
      

        
