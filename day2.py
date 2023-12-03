
def readFile(file): 
    f = open(file)
    return f.readlines()

def isPossible(line): 
    lineList = line.split("; ")
    print(lineList)


def main(): 
    file = readFile("input2.txt")
    index = 1
    result = 0
    for line in file:
        if isPossible(line):
            result += index
        index += 1


main()

