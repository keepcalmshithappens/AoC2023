
def main(): 
    lines = open("example.txt").readlines()
    resultD = {}
    card = 0
    for line in lines: 
        card += 1
        finalResult = 0

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
                index += 1
            #print("result", result)
        if result: 
            finalResult += 2**(result-1)
            for i in range(finalResult): 
                key = card + i + 1
                if key > len(lines):
                    continue
                if not key in resultD:
                    resultD[key] = [1]
                else: 
                    resultD[key].append(1)
            if card == 1: 
                continue
            for k in range(len(resultD[card])): 
                key = card + k
                print(card)
                if key > len(lines):
                    continue
                if not key in resultD:
                    resultD[key] = [1]
                else: 
                    resultD[key].append(1)
                print(winner, resultD[key], key)
    final = 0
    for key in resultD: 
        for i in resultD[key]: 
            final += 1
    print(final)




        #print("finalresult ", finalResult)




main()
