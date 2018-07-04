import sys

def main():
    command = sys.argv[1]

    if(command == "add"):
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x + y)
    if(command == "sub"):
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x-y)



if __name__ == "__main__":
    main()