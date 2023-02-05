#class for making a queue
class queue:
    first_pointer = -1
    last_pointer = -1
    queue_size = 10
    #contructor
    def __init__(self) -> None:
        self.queue = []

    #was made to add elements to the  back of the queue
    def enqueue(self, number):
        if not self.isFull():
            self.queue.append(number)
            self.last_pointer += 1
            print(self.queue)
            if self.first_pointer == -1:
                self.first_pointer += 1
        else:
            return "not possible,\nthe queue is full!"
    
    #was made to remove the front element of the queue
    def dequeue(self):
        if not self.isEmpty():
            print(self.queue.pop(self.first_pointer))
            print(self.queue)
            if self.first_pointer > self.last_pointer:
                self.first_pointer = -1
                self.last_pointer = -1
        else:
            return "not possible,\nthe queue is empty!"

    #was made to check if queue could add more numbers in to it
    def isEmpty(self):
        if self.last_pointer == -1:
            return True
        else:
            return False

    #was made to check if the queue has no value and can not remove any numbers from it
    def isFull(self):
        if self.last_pointer == self.queue_size:
            return True
        else:
            return False

    #displays the front value of the queue
    def peek(self):
        if not self.isEmpty():
            return self.queue[self.first_pointer]

#class for making a queue

if __name__ == "__main__":
    #some tests for the functoinality of the whole DataStructure
    queue_obj = queue()
    print(queue_obj.isEmpty())
    queue_obj.enqueue(int(input("input:")))
    queue_obj.enqueue(int(input("input:")))
    queue_obj.enqueue(int(input("input:")))
    queue_obj.dequeue()
    queue_obj.dequeue()
    queue_obj.dequeue()
    queue_obj.enqueue(int(input("input:")))
    print(queue_obj.isEmpty())
    print(queue_obj.peek())