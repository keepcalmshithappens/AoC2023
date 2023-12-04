   

def main(): 
    lines = open("input4.txt").readlines()
    for line in lines: 
        line = line.split(": ")[1]
        winner = line.split("| ")[0]
        mine = line.split("| ")[1]
        mine = mine.split(" ")
        winner = winner.split(" ")
        finalResult = 0
        for i in winner:
            index = 0
            result = 0
            for nr in mine:
                if nr == i:
                    print(i, nr)
                    result += 1
                    mine.remove(nr)
        finalResult += 2**result 
    #print(finalResult)
main()


