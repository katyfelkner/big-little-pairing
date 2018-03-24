import csv
import copy

bigPrefPath = './bigtest.csv'
littlePrefPath = './littletest.csv'
resultPath = './BLtestresults.txt'

# form matrices from csv(s)
with open(bigPrefPath, encoding='utf-8') as bigFile, open(littlePrefPath, encoding='utf-8') as littleFile, open(resultPath, mode='w') as resultFile:
    bigList = list(csv.reader(bigFile))
    littleList = list(csv.reader(littleFile))
    numRows = len(bigList)
    numCols = len(bigList[0])

    prefList = [None for x in range(numRows)]
    # copy big names over
    prefList[0] = copy.deepcopy(bigList[0])  # check that this copies correctly

    # add matrices
    # assumes matrices have same dimensions
    for i in range(1, numRows):
        prefList[i] = [0 for x in range(numCols)]
        # copy the little's name over
        prefList[i][0] = copy.deepcopy(littleList[i][0])

        # now add pref numbers to create the preference matrix
        for j in range(1, numCols):
            prefList[i][j] = int(bigList[i][j]) + int(littleList[i][j])

    # prefList is now a complete pref matrix
    # search for sums of 2 (i.e. a mutual first pref)
    # output those and set to 0
    # search for 3 (i.e. little's first choice, big's second choice)
    # output those and set to 0
    # search for 4 (is this ambiguous?)

    for k in range(2, 10):
        for r in prefList:
            if r[0] == '':
                continue
            for i in range(1, numCols):
                if int(r[i]) == k:
                    # it's a mutual first pref! yay!
                    resultFile.write("Big/Little Pair: " + str(prefList[0][i]) + " and " + str(r[0]) + "\n")
                    # after they are paired, set the whole row and column to 0
                    for j in range(1, numCols):
                        r[j] = 0
                    for j in range(1, numRows):
                        prefList[j][i] = 0
                    break

    # now we have printed all the pairs we can find
    # lets print a list of unpaired bigs and unpaired littles, if there are any
    # unpaired bigs first
    resultFile.write("Unpaired Bigs:\n")
    for i in range(1, numCols):
        for j in range(1, numRows): # need check all rows b/c one 0 does not guarantee unpaired
            if prefList[j][i] != 0:
                resultFile.write(str(prefList[0][i] + "\n"))
                break
            # if all values are 0 nothing is output

    # now output unpaired littles
    resultFile.write("Unpaired Littles:\n")
    for i in range(1, numRows):
        if not all(j==0 for j in prefList[i][1:]):
            resultFile.write(str(prefList[0][i] + "\n"))





