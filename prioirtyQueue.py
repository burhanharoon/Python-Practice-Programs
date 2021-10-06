# THE GREATER THE VALUE, THE GREATER THE PRIORITY

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
        print("-> Pushed {} to queue".format(x))
        self.array.sort()
        self.array.reverse()

    def dequeue(self):
        print("-> Popped {} from the queue".format(self.array.pop())) if not self.isEmpty() else print("-> Cant Dequeue Empty Queue")

    def peek(self):
        print("-> Peek: ", self.array[self.head])

    def displayQueue(self):
        print("-> Displaying Queue: {}".format(self.array[self.head:self.tail+1]))


s = queue()
s.enqueue(1)
s.enqueue(2)
s.displayQueue()
s.peek()
s.enqueue(3)
s.enqueue(4)
s.displayQueue()
s.dequeue()
s.peek()
s.dequeue()
s.peek()
s.displayQueue()
s.dequeue()
s.displayQueue()
s.dequeue()
s.displayQueue()
s.dequeue()
s.displayQueue()