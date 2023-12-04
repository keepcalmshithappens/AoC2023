import re

def input(file): 
    f = open(file)
    x = f.readlines()
    return [line[:-1] for line in x] 

def checkSurrounding(index, lineIndex, lines): 
    
    miny = lineIndex
    if lineIndex > 0: 
        miny = lineIndex - 1
    maxy = lineIndex
    if lineIndex < len(lines)-1: 
        maxy = lineIndex + 1
    minx = index
    if index > 0: 
        minx = index - 1
    maxx = index
    if index < len(lines[0])-1: 
        maxx = index + 1
    #print(minx, index, maxx)
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            if not lines[y][x].isnumeric() and lines[y][x] != ".": 
                print("done!!\n")
                return True
    return False

def main(): 
    lines = input("input3.txt")
    
    lineIndex = 0
    li = []
    for line in lines:
        index = 0
        num = ""
        okay = False
        for char in line:
            if char.isnumeric(): 
                num += char
                #print(index, lineIndex)
                if checkSurrounding(index, lineIndex, lines):
                    okay = True
            elif num != False: 
            #    print(num)
                if okay:     
                    li.append(num)
                    okay = False
                num = ""
            index += 1
        lineIndex += 1
    result = 0
    print(li)
    for i in li:
        #print(i)
        result += int(i)
    print(result)


main()
