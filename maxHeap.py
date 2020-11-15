side_select = 0
mainheap = []


class Node:
    def __init__(self, data=None):
        self.nodedata = data
        self.r_child = None
        self.l_child = None
        self.node_l_member = 0
        self.node_r_member = 0


class MaxHeap:
    def __init__(self, data=None):
        self.rootdata = data
        self.root_r_member = 0
        self.root_l_member = 0
        self.root_r_child = None
        self.root_l_child = None

    def insert(self, data):
        global mainheap
        if data not in mainheap:
            mainheap.append(data)
            if self.root_insert_check(data):
                return
            else:
                if self.root_l_member <= self.root_r_member:
                    self.root_l_member += 1
                    self.side_add(data, self.root_l_child)
                    return
                else:
                    self.root_r_member += 1
                    self.side_add(data, self.root_r_child)
                    return
        else:
            print(str(data)+"in heap")
            return

    def root_insert_check(self, data):
        global mainheap
        if self.rootdata:
            if self.rootdata < data:
                arranged = mainheap
                mainheap = []
                arranged.sort(reverse=True)
                self.delet_root()
                for i in arranged:
                    self.insert(i)
                return True
            else:
                if self.root_l_child and self.root_r_child:
                    return False
                elif self.root_l_child is None:
                    NewNode = Node(data)
                    self.root_l_child = NewNode
                    self.root_l_member += 1
                    return True
                elif self.root_r_child is None:
                    NewNode = Node(data)
                    self.root_r_child = NewNode
                    self.root_r_member += 1
                    return True
        else:
            self.rootdata = data
            return True

    def side_add(self, data, node):
        global side_select
        if node.node_r_member == 0:
            newnode = Node(data)
            node.r_child = newnode
            node.node_r_member += 1
            return
        elif node.node_l_member == 0:
            newnode = Node(data)
            node.l_child = newnode
            node.node_l_member += 1
            return
        else:
            if node.r_child.node_r_member < node.l_child.node_r_member:
                self.side_add(data, node.r_child)
            elif node.r_child.node_r_member > node.l_child.node_r_member:
                self.side_add(data, node.l_child)
            elif node.r_child.node_l_member < node.l_child.node_l_member:
                self.side_add(data, node.r_child)
            elif node.r_child.node_l_member > node.l_child.node_l_member:
                self.side_add(data, node.l_child)
            else:
                if side_select == 0:
                    side_select = 1
                    self.side_add(data, node.r_child)
                else:
                    side_select = 0
                    self.side_add(data, node.l_child)

    def delet_root(self):
        self.rootdata = None
        self.root_l_child = None
        self.root_r_child = None
        self.root_l_member = 0
        self.root_r_member = 0
        return

    def re_arrenge(self):
        global mainheap
        arrengeheap = mainheap
        mainheap = []
        maximum = max(mainheap)
        mainheap.remove(maximum)
        arrengeheap = mainheap
        mainheap = []
        arrengeheap.sort(reverse=True)
        self.delet_root()
        for i in arrengeheap:
            self.insert(i)
        return

    def extract(self):
        data = self.rootdata
        self.re_arrenge()
        return data

    def prinroot(self):
        if self.rootdata and self.root_l_member > 0 and self.root_r_member == 0:
            print(str(self.rootdata)+"  is root")
            print(str(self.root_l_child.nodedata)+"is left child of root")
            return False
        elif self.rootdata and self.root_l_member == self.root_r_member == 0:
            print(str(self.rootdata)+"  is root")
            return False
        elif self.rootdata and self.root_r_member > 0 and self.root_l_member == 0:
            print(str(self.rootdata)+"  is root")
            print(str(self.root_r_child.nodedata)+"is right child of root")
            return False
        else:
            print(str(self.rootdata)+"  is root")
            print(str(self.root_l_child.nodedata)+"is left child of root")
            print(str(self.root_r_child.nodedata)+"is right child of root")
            return True

    def printnodes(self, node):
        if node.l_child:
            print(str(node.l_child.nodedata) +
                  " is left child of " + str(node.nodedata))
        if node.r_child:
            print(str(node.r_child.nodedata) +
                  " is right child of " + str(node.nodedata))
        if node.l_child:
            if node.l_child.node_l_member > 0 or node.l_child.node_r_member > 0:
                self.printnodes(node.l_child)
        if node.r_child:
            if node.r_child.node_l_member > 0 or node.r_child.node_r_member > 0:
                self.printnodes(node.r_child)
        return

    def printheap(self):
        if self.prinroot():
            if self.root_r_child.r_child or self.root_r_child.l_child:
                self.printnodes(self.root_r_child)
            if self.root_l_child.r_child or self.root_l_child.l_child:
                self.printnodes(self.root_l_child)
            return
        else:
            return
