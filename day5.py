
def getseeds(line):
    num = ""
    result = []
    for char in line: 
        if char.isnumeric():
            num += char
        else: 
            if num: 
                result.append(num)
                num = ""
    return result


def get_numbers(numList): 
    pass        



def main(): 
    lines = open("example.txt").readlines()
    sts = {}
    stf = {}
    ftw = {}
    wtl = {}
    ltt = {}
    tth = {}
    htl = {}
    masterList = [sts, stf, ftw, wtl, ltt, tth, htl]
    result = []
    listIndex = 0
    for line in lines: 
        if "seeds:" in line: 
            result = getseeds(line)
            continue
        if "seed-to-soil map:" in line: 
            continue
        if "soil-to-fertilizer map:" in line: 
            listIndex = 1
            continue
        if "fertilizer-to-water map:" in line: 
            listIndex = 2
            continue
        if "water-to-light map:" in line:
            listIndex = 3
            continue
        if "light-to-temperature map:" in line: 
            listIndex = 4
            continue
        if "temperature-to-humidity map:" in line: 
            listIndex = 5
            continue
        if "humidity-to-location map:" in line: 
            listIndex = 6
            continue
        if line.isspace():
            continue
        lista = getseeds(line)
        iterations = int(lista[2])
        first_start = int(lista[0])
        second_start = int(lista[1])
        for i in range(iterations):
            masterList[listIndex][first_start+i] = second_start+i
            
    for seed in result:
        print(seed)
main()


