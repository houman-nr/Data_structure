#creating a linked list

#this class was created bc we wanted to creat a node for every time a new element is added to the linked list
class Node:

    def __init__(self, inputData, nextElement):
        self.data = inputData
        self.nextElement = nextElement

#this class was created bc we had to organize the inputs of the list through some functions for each functionality
class Linked_list:
    last_pointer = None
    head = None
    next_head = None

    def __init__(self, inputData):
        nodeObj = Node(inputData, self.last_pointer)
        self.head = nodeObj.data
        self.last_pointer = nodeObj.nextElement

    def add_item(self, inputData):
        nodeObj = Node(inputData)
        self.last_pointer = nodeObj.data

    def show_item(self):
        while(True):
            pointer = self.hea
            print()



#creating a linked list

if __name__ == "__main__":
    linkedObj = Linked_list(int(3))
    linkedObj.add_item(int(input("type your input into the linked list")))
