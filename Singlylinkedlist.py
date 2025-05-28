
class node:
    def __init__(self,value):
        self.value=value
        self.next=None
class linkedlist:
    def __init__(self):
        self.head = None
    def insertatthebeginning(self,new_data):
        new_node = node(new_data)
        new_node.next= self.head

        self.head = new_node
    def insertattheend(self,new_data):
        new_node = node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node
    def deletefromtheend(self):
        if self.head is None:
            return 'List is empty'
        if self.head.next is None:
            self.head =None
            return
        temp = self.head
        while temp.next.next:
            temp =temp.next
        temp.next = None

    def deletefromthebeginning(self):
        if self.head is None:
            return 'List is empty'
        self.head = self.head.next


    def printlinkedlist(self):
        temp = self.head

        while temp:
            print(temp.value, end = ' ')
            temp = temp.next
        print()


if __name__ == '__main__':
      llist = linkedlist()
      llist.insertatthebeginning('fox')
      llist.insertatthebeginning('brown')
      llist.insertatthebeginning('quick')
      llist.insertatthebeginning('The')
      llist.printlinkedlist()
      llist.insertattheend('jumps')
      llist.printlinkedlist()
      llist.deletefromtheend()
      llist.deletefromthebeginning()
      llist.printlinkedlist()

      llist.insertatthebeginning('A')
      llist.printlinkedlist()