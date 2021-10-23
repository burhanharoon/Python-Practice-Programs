class stack:
    def __init__(self):
        self.array = []

    def isEmpty(self):
        if int(len(self.array)-1) <= -1:
            return True
        else:
            return False

    def pushToStack(self, x):
        self.array.append(int(x))
        print("Pushed {} to stack".format(x))

    def popFromStack(self):
        print("Stack Underflow") if self.isEmpty() else print(
            "Popped {} from the stack".format(self.array.pop()))

    def topOfStack(self):
        topElement = int(len(self.array)-1)
        print("Top: ", self.array[topElement]) if self.isEmpty(
        ) == False else print("Stck Empty")

    def displayStack(self):
        print("Stack Empty") if self.isEmpty() else print(
            "Dispaying Stack: ", self.array)


s = stack()
s.pushToStack(1)
s.displayStack()
s.pushToStack(2)
s.pushToStack(3)
s.topOfStack()
s.displayStack()
s.popFromStack()
s.topOfStack()
s.popFromStack()
s.popFromStack()
s.popFromStack()
s.displayStack()
print(s.isEmpty())
