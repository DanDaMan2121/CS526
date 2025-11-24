import sys

def stableMatching(menDict, womenDict):
    freeMen = list(menDict.keys())
    proposalsMade = {man: [] for man in menDict}
    womenPartner = {woman: None for woman in womenDict}
    womenRank = {
        woman: {man: rank for rank, man in enumerate(prefs)}
        for woman, prefs in womenDict.items()
    }

    while freeMen:
        man = freeMen.pop(0)
        manPrefList = menDict[man]
        for woman in manPrefList:
            if woman not in proposalsMade[man]:
                proposalsMade[man].append(woman)
                if womenPartner[woman] is None:
                    womenPartner[woman] = man
                else:
                    currentPartner = womenPartner[woman]
                    if womenRank[woman][man] < womenRank[woman][currentPartner]:
                        womenPartner[woman] = man
                        freeMen.append(currentPartner)
                    else:
                        freeMen.append(man)
                break

    manToWoman = {man: woman for woman, man in womenPartner.items()}
    return manToWoman








if __name__ == '__main__':

    if len(sys.argv) > 1:
        fileName = sys.argv[1]
        myDict = dict()
        menDict = dict()
        womenDict = dict()
        size = 0
        with open (fileName, 'r') as file:
            for i, line in enumerate(file):
                myLine = line.strip('\n')
                if i == 0:
                    size = int(myLine)
                else:
                    myList = myLine.split(' ')
                    name = myList[0]
                    if i < size + 1:
                        menDict[name] = myList[1:]
                    else:
                        womenDict[name] = myList[1:]
 
        myDict = stableMatching(menDict, womenDict)
     
        if len(sys.argv) > 2:
            allMatched = True
            fileName = sys.argv[2]
            with open(fileName, 'r') as file:
                for i, line in enumerate(file):
                    myLine = line.strip('\n')
                    myList = myLine.split(' ')
                    # print(myList)
                    name1 = myList[0]
                    name2 = myList[1]
                    currentPerson = myDict[name1]
                    if currentPerson != name2:
                        allMatched = False
                        break
                    print(f"My Match {name1} : {myDict[name1]}")
                    print(f"Your Match {name1} : {name2}")
            
            if allMatched:
                print('YOUR ANS == MY ANS')
            else:
                print('YOUR ANS != MY ANS')

            