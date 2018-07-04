import sys
import math

def pythag(a, b):
    a_squared = math.pow(a, 2)
    b_squared = math.pow(b, 2)

    added = a_squared + b_squared

    return math.sqrt(added)

def main():
    userInput = sys.argv[1]

    if userInput == "add":
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x+y)

    if (userInput == "sub"):
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x - y)

    if(userInput == "mod"):
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x % y)

    if(userInput == "mult"):
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x * y)

    if(userInput == "div"):
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x / y)

    if(userInput == "countto"):
        x = int(sys.argv[2])

        for i in range(x+1):
            print(i)

    if(userInput == "hypot"):
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(pythag(x,y))





if __name__ == "__main__":
    main()