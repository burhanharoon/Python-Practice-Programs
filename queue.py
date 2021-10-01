class queue:
    def __init__(self):
        self.array = []
        self.head = int(0)
        self.tail = int(0)

    def isEmpty(self):
        if int(len(self.array)-1) <= -1:
            return True
        else:
            return False

    def enqueue(self, x):
        self.array.insert(self.tail, int(x))
        self.tail += 1
        print("Pushed {} to stack".format(x))

    def dequeue(self):
        print("Popped {} from the stack".format(self.array.pop(self.head)))
        print("head",self.head)

    def peek(self):
        print("peek",self.array[self.head])

    def displayStack(self):
        print(self.array[self.head:self.tail+1])


s=queue()
s.enqueue(1)
s.enqueue(2)
s.displayStack()
s.peek()
s.enqueue(3)
s.enqueue(4)
s.displayStack()
s.dequeue()
s.dequeue()
s.peek()
s.displayStack()