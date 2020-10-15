# linked lists
# create one direction node
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None

    # listprint function: first print (first member of the linked List) and we use nextval (as address)

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    # add new Node at the first
    # NewNode created with Node class with value (newdata),
    # we change the address
    # Node("A") is first
    # we have to insert this address to our new Node and we set NewNode  first
    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode
    # add new Node at the End
    # NewNode Create with Node Class with value(newdata)
    # if variable address is none ==> linked list have 0 or 1 member and we can add this node
    # we create lastnode variable for find the last node , and And with the initial value (first headval address)
    # while nextval not none , we are going to find the last

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval == Node:
            self.headval = NewNode
            return
        else:
            lastnode = self.headval
            while(lastnode.nextval):
                lastnode = lastnode.nextval
            lastnode = NewNode

    # we create a valiable lastnode1 for find the address
    # if given address is none ,print is absent
    # if lastnode1 is none ==> first address and we added to first place
    # while given address is not equal to lastnode1 we pass the list until find it
    # when find correct node
    # we take his nextvalue address and give to newnode
    # and give him newnode address for next value
    def Inbetween(self, newdata, lastnode):
        NewNode = Node(newdata)
        lastnode1 = self.headval
        if lastnode == None:
            print("The mentioned node is absent")
        elif lastnode1 == None:
            self.headval = NewNode
            return
        else:
            while(lastnode1.nextval != lastnode):
                lastnode1 = lastnode1.nextval
            NewNode.nextval = lastnode1.nextval
            lastnode1.nextval = NewNode

    # firstnode == headnode variable
    # if our reqested value in first node , we set next node as first and remove that node
    # while headnode value not equall to our requested value we pass the list
    # we created lastnode for change address to next node
    # then we addressed the lastnode to next node
    # and remove node
    def RemoveNode(self, nValue):
        headNode = self.headval
        if headNode == None:
            return
        elif headNode.nextval is not None and headNode.dataval == nValue:
            self.headval = headNode.nextval
            headNode = None
            return
        else:
            while(headNode.dataval != nValue):
                lastnode = headNode
                headNode = headNode.nextval
            lastnode.nextval = headNode.nextval
            headNode = None
