
def readFile(file): 
    f = open(file)
    return f.readlines()


def isPossible(line):
    lineList = line.split("; ")
    maxRed = 1
    maxBlue = 1
    maxGreen = 1
    for draw in lineList:
        color = draw.split(", ")
        for i in color:
            #print(i)
            number = i.split(" ")
            if "\n" in number[1]: 
                number[1] = number[1][:-1]
            #print(number)
            if "red" in number: 
                if int(number[0]) > maxRed: 
                    maxRed = int(number[0])
            if "blue" in number: 
                if int(number[0]) > maxBlue: 
                    maxBlue = int(number[0])
            if "green" in number: 
                if int(number[0]) > maxGreen: 
                    maxGreen = int(number[0])
    
    #print(maxRed, maxGreen, maxBlue)
    #print(maxRed*maxGreen*maxBlue)
    return maxRed*maxGreen*maxBlue



def main(): 
    file = readFile("input2.txt")
    index = 1
    result = 0
    result2 = 0
    for line in file:
        x = line.split(": ")
        line = x[1]
        #print(line)
        if isPossible(line):
            result += index
            result2 += isPossible(line)
            print(index)
            print(isPossible(line))
            print(result2)
            print("\n")
        index += 1
    print(result2)
    #print(result)
main()







