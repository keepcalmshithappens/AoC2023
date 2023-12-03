
def readFile(file): 
    f = open(file)
    return f.readlines()


def isPossible(line):
    lineList = line.split("; ")
    #print(lineList)
    for draw in lineList:
        #print(draw)
        color = draw.split(", ")
        for i in color:
            number = i.split(" ")
            #print(number[0])
            if "red" in number: 
                if int(number[0]) >12: 
                    return False
            if "blue" in number: 
                if int(number[0]) > 14: 
                    return False
            if "green" in number: 
                if int(number[0]) > 13: 
                    return False
    return True



def main(): 
    file = readFile("input2.txt")
    index = 1
    result = 0
    for line in file:
        x = line.split(": ")
        line = x[1]
        if isPossible(line):
            result += index
        index += 1
    print(result)

main()

