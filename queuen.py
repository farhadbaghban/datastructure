# queens
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
# is empty test
print(q.isEmpty())
# enqueue
q.enqueue(1)
q.enqueue('DOG')
q.enqueue(True)
q.enqueue(2)
print(q.isEmpty())
print(q.size())
# dequeue
print(q.dequeue())
print(q.size())
print(q.dequeue())
print(q.size())
print(q.dequeue())
print(q.size())
print(q.dequeue())
print(q.size())
print(q.isEmpty())
