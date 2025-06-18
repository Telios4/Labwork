class circular_queue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * circular_queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0


    def __len__(self):
        return self._size

    def is_Empty(self):

        return self._size == 0

    def first(self):
       if self.is_Empty():
           raise Empty('Queue is empty')
       return self._data[self._front]

    def dequeue(self, data):
        if self.is_Empty():
            raise Empty('Queue is empty for dequeue operation')
        front = (self._front + 1) % len(self._data)
        dequeue_element = self._data[self._front]
        self._data[self._front] = None
        self._size -= 1


    def enqueue(self, element):
        if self._size == len(self._data):
            self._resize(2 + len(self._data))
        tail = (self._front + self._size) % len(self._data)
        self._data[tail] = element
        self._size = self._size+ 1


    def resize(self, new_capacity):
        ...
class Empty(Exception):
    pass
if __name__ == '__main__':
    object_queue = circular_queue()

    insert_element = [11,22,33,44,55]

    for element in insert_element:
        object_queue.enqueue(element)

        print (f"Added element: {element}")
        print (f"The new size of the queues :{len(object_queue) }")