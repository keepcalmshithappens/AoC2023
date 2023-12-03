
def input(file): 
    read = open(file)
    return read.readlines()

def check(line):
    if line[0:3] == "one": 
        return "1"
    elif line[0:3] == "two": 
        return "2"
    elif line[0:5] == "three":
        return "3"
    elif line[0:4] == "four": 
        return "4"
    elif line[0:4] == "five":
        return "5"
    elif line[0:3] == "six": 
        return "6"
    elif line[0:5] == "seven": 
        return "7"
    elif line[0:5] == "eight":
        return "8"
    elif line[0:4] == "nine":
        return "9"
    else:
        return None


def main(): 
    file = input("day1Input.txt")
    resultList = []
    for line in file: 
        numbers = []
        checkLine = line
        for char in line: 
            if char.isnumeric(): 
                numbers.append(char)
            #print(check(checkLine))
            if check(checkLine) != None: 
                numbers.append(check(checkLine))
            checkLine = checkLine[1:]
        resultList.append(numbers[0] + numbers[len(numbers)-1])
    print(resultList)
    result = 0
    for i in resultList: 
        result += int(i)
    print(result)


main()


