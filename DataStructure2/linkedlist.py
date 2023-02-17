#creating a linked list

#this class was created bc we wanted to creat a node for every time a new element is added to the linked list
class Node:

    def __init__(self, inputData, nextElement):
        self.data = inputData
        self.nextElement = nextElement

#this class was created bc we had to organize the inputs of the list through some functions for each functionality
class Linked_list:

    def __init__(self, nodeObj):
        self.head = nodeObj
        self.last_node = nodeObj
        self.first_node = nodeObj

    def delet_start(self):
        self.head = self.head.nextElement

    def delet_end(self):
        currentVal = self.head
        while currentVal.nextElement != self.last_node:
            currentVal = currentVal.nextElement
        currentVal.nextElement = None

    def delet_by_index(self, index):
        i = 0
        currentEl = self.head
        while i != index-1:
            currentEl = currentEl.nextElement
            i += 1
        nextEl = currentEl.nextElement
        nextEl = nextEl.nextElement
        currentEl.nextELement = nextEl
        

    def add_end(self, nodeObj):
        self.last_node.nextElement = nodeObj
        self.last_node = nodeObj

    def add_start(self, nodeObj):
        nodeObj.nextElement = self.first_node
        self.head = nodeObj
        self.first_node = nodeObj

    def add_by_index(self, nodeObj, index):
        i = 0
        currentEl = self.head
        while i != index:
            currentEl = currentEl.nextElement
            i += 1
        nextEl = currentEl.nextElement
        currentEl.nextElement = nodeObj
        nodeObj.nextElement = nextEl

    def show_list(self):
        currentVal = self.head
        while currentVal != None:
            print(currentVal.data)
            currentVal = currentVal.nextElement

#creating a linked list

if __name__ == "__main__":
    linkedObj = Linked_list(Node(int(0), None))
    linkedObj.add_end(Node(int(1), None))
    linkedObj.add_end(Node(int(2), None))
    linkedObj.add_end(Node(int(4), None))
    linkedObj.add_end(Node(int(5), None))
    linkedObj.add_start(Node(int(-1), None))
    linkedObj.add_by_index(Node(int(3), None), 3)
    linkedObj.delet_start()
    linkedObj.delet_by_index(int(2))
    linkedObj.show_list()