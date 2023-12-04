
def main(): 
    lines = open("input4.txt").readlines()
    finalResult = 0
    for line in lines: 
        line = line.split(": ")[1]
        winner = line.split("| ")[0]
        mine = line.split("| ")[1]
        mine = mine.split(" ")
        winner = winner.split(" ")
        result = 0
        for i in winner:
            if i == '':
                continue
            index = 0
            for nr in mine:
                if index == len(mine)-1: 
                    nr = nr[:-1]
                if nr == i:
                    result += 1
                    #mine.remove(mine[index])
                index += 1
            print("result", result)
        if result: 
            finalResult += 2**(result-1) 
        print("finalresult ", finalResult)

main()
