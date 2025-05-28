from symtable import Class


class Singlylinkedlist:
    def __init__(self,value,Nextnode = None):
       self.value = value
       self.Nextnode = Nextnode


snode1=Singlylinkedlist(1,None)
snode2=Singlylinkedlist(2,None)
snode3=Singlylinkedlist(3,None)
snode4=Singlylinkedlist(4,None)



snode1.Nextnode=snode2
snode2.Nextnode=snode3
snode3.Nextnode=snode4

currentnode=snode1
while True:
    print(currentnode.value, ">>>", end = ' ')

    if currentnode.Nextnode is None:
        print("None")
        break
    currentnode=currentnode.Nextnode

