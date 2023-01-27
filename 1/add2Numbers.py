#taking two numbers and calculation the sumation of the those two numbers
import math


def add2numbers():
    num1 = num2 =sumation = int(0)
    num1, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    sumation = num1 + num2
    print(sumation)
#taking two numbers and calculation the sumation of the those two numbers

#find the biggest out of three inputs 
def findBiggestOf3():
    a ,b ,c = input().split()
    a ,b ,c = int(a), int(b), int(c)
    biggestN = int(-10000)
    for i in (a, b, c):
        if i > biggestN:
            biggestN = i
    return biggestN
#find the biggest out of three inputs 

#find the roots of Quadratic equation
def QuadraticEqu():
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    delta = math.sqrt(int(b**2 - 4*a*c))
    root1 = int((-b - delta)/2*a)
    root2 = int((-b + delta)/2*a)
    return [root1, root2]

#find the roots of Quadratic equation


if __name__ == "__main__":
    pass
