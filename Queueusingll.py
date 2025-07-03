class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self, value):
        self.front = None
        self.rear = None
        self.size = 0
    def __len__(self):
        return self.size
    def __repr__(self):
        items = []
        current = self.front
        while current is not None:
            items.append(str(current.data))
            current = current.next
        return ', '.join(items)
    def enqueue(self, value):
        new_node = node(value)
        if self.rear is None:
            self.front = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    def dequeue(self):
        if self.front is None:
            raise IndexError('Queue is empty')
        dequeue_value = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        self.size -= 1
        return dequeue_value
    def peek(self):
        if self.front is None:
            raise IndexError('Queue is empty')
        return self.front.value
    def is_Empty(self):
        return self.front is None
if __name__ == '__main__':
    q = Queue(1)
    q.enqueue(11)
    q.enqueue(22)
    q.enqueue(33)
    q.enqueue(44)
    q.enqueue(55)
    q.enqueue(66)

    print(q)
    print(len(q))

    print(q.dequeue())
    print(q.dequeue())

    print(q)
    print(len(q))

