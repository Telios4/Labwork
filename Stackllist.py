class stacknode:
    def __init__(self,value):
        self.value=value
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def is_empty(self):
      return self.top == None
    def push(self,value):
        new_node=stacknode(value)
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop an empty stack")
        popped_value=self.top.value
        self.top=self.top.next
        return popped_value
    def peek(self):
        if self.is_empty():
            raise Exception("Cannot peek an empty stack")
        return self.top.value
    def display(self):
        current=self.top
        values=[]
        while current:
            values.append(current.value)
            current=current.next
            print("Stack from top to bottom:", "->".join(values))
if __name__=="__main__":
    stack_ll=linkedlist()
    stack_ll.push(10)
    stack_ll.push(23)
    stack_ll.push(34)

    stack_ll.display()

    print("Peek top:", stack_ll.peek())
    print("Pop top:", stack_ll.pop())
    stack_ll.display()