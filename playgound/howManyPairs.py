def main():
    students = ['Bob', 'Sally', 'Doug', 'Rachel', 'Drew', 'Paula', 'Dave', 'Ralph', 'Stanley', 'Wendy', 'Marrisa']

    if((len(students) % 2) == 0):
        print("Even Number of Groups")
        print(len(students)/2)
        print("Number of groups")
    else:
        print("Odd number of groups")
        print(int(len(students)/2))
        print("Number of groups, with one group of 3.")


if __name__ == "__main__":
    main()