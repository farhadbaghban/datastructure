# create node with 2 address value
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        self.pervval = None


class doubly_linked_list:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        if self.headval == None:
            self.headval = NewNode
        else:
            NewNode.pervval = self.headval.pervval
            NewNode.nextval = self.headval
            self.headval.pervval = NewNode
            self.headval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        EndNode = self.headval
        while(EndNode.nextval != None):
            EndNode = EndNode.nextval
        NewNode.nextval = EndNode.nextval
        EndNode.nextval = NewNode
        NewNode.pervval = EndNode

    def Inbetween(self, newdata, lastnode):
        NewNode = Node(newdata)
        Between = self.headval
        while(Between.dataval != lastnode):
            Between = Between.nextval
        nextnode = Between.nextval
        NewNode.nextval = nextnode
        NewNode.pervval = Between
        Between.nextval = NewNode
        nextnode.pervval = NewNode

    def RemoveNode(self, nValue):
        headNode = self.headval
        if headNode == None:
            return
        elif headNode.dataval == nValue:
            headNode = None
            return
        else:
            while(headNode.dataval != nValue):
                lastnode = headNode
                headNode = headNode.nextval
            nextnode = headNode.nextval
            lastnode.nextval = nextnode
            nextnode.pervval = lastnode
            headNode = None
