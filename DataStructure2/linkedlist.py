#creating a linked list

#this class was created bc we wanted to creat a node for every time a new element is added to the linked list
class Node:

    def __init__(self, inputData, nextElement):
        self.data = inputData
        self.nextElement = nextElement

#this class was created bc we had to organize the inputs of the list through some functions for each functionality
class Linked_list:

    def __init__(self, nodeObj):
        print(nodeObj.data)
        self.head = nodeObj
        self.last_node = nodeObj

    def add_end(self, nodeObj):
        self.last_node.nextElement = nodeObj
        self.last_node = nodeObj

    def show_list(self):
        currentVal = self.head
        while currentVal != None:
            print(currentVal.data)
            currentVal = currentVal.nextElement

#creating a linked list

if __name__ == "__main__":
    print(Node(123, None))
    linkedObj = Linked_list(Node(int(123), None))
    linkedObj.add_end(Node(int(1), None))
    linkedObj.add_end(Node(int(3), None))
    linkedObj.add_end(Node(int(5), None))
    linkedObj.add_end(Node(int(7), None))
    linkedObj.show_list()