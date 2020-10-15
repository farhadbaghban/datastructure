# stack

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    # i use the append because, append add the value at last
    # as well as , i can use the extend
    # append can take more than 1 value(in this case we dont need it)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    # peek get the top member from the stack BUT dont remove

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


stack = Stack()
print(stack.isEmpty())
stack.push(2)
stack.push('tiger')
stack.push('egg')
stack.push(23)
stack.push(False)
print(stack.isEmpty())
print(stack.size())
print("____________")
print(stack.peek())
stack.pop()
print("____________")
print(stack.peek())
print("____________")

print(stack.size())
print("____________")
