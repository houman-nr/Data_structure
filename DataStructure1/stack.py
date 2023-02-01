#making a stack
class stack:
    top = 0
    max = 0

    #constructore for the stack
    def __init__(self, stack_volume):
        self.stack = []
        self.top = 0
        self.max = stack_volume
    #takes a number to add it to the end of the stack
    def push(self, number):
        if self.top < self.max:
            self.stack.append(number)
            self.top += 1
            print(self.stack)
        else:
            print("stack is full! \nplease pop some elements first")
    #will pop out the last number which was added to the stack
    def pop(self):
        if 0 < self.top:
            self.stack.remove(self.top)
            self.top -= 1
            print(self.stack)
        else:
            print("the stack is empty! \nplease add some items to the stack first")

    def isEpmty(self):
        if 0 < self.top:
            return False
        else:
            return True
    
    def isFull(self):
        if self.top < self.max:
            return False
        else:
            return True
    
    def peek(self):
        if self.isEpmty == False:
            return self.stack[self.top - 1]
        else:
            return "There isn't anything to be peeked at!"
#making a stack

if __name__ == "__main__":
    stack_obj = stack(10)
    stack_obj.push(1)
    stack_obj.pop()
    print(stack_obj.isEpmty())
    print(stack_obj.peek())