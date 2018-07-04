
def main():
    grid = [['S','F','F','F'],['F','H','F','H'],['F','F','F','H'],['H','F','F','E']]
    for c in grid:
        row = ""
        for r in c:
            row+=r
        print(row)


if __name__ == "__main__":
    main()