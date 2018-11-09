#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import csv
import collections as collect


def dictBinarySearchAndInsert(key, val, _unsortedDict):
    _unsortedDict[key].sort()
    low = 0
    hi = len(_unsortedDict[key])-1
    while low <= hi:
        mid = int(low + (hi-low)/2)
        #print("low is:" + str(low) + "high is " + str(hi) + "mid is" + str(mid))
        if val == _unsortedDict[key][mid]:
            return
        elif val < _unsortedDict[key][mid]:
            hi = mid-1
        elif val > _unsortedDict[key][mid]:
            low = mid + 1

    _unsortedDict[key].append(val)


nodeHeroDict = {}#collect.OrderedDict()
nodeComicDict = {}#collect.OrderedDict()
#https://docs.python.org/3.7/library/csv.html
with open('nodes.csv', 'r') as nodefile:
    next(nodefile)
    nodeReader = csv.reader(nodefile, delimiter=',')
    for row in nodeReader:
        if row[1] == 'comic':
            nodeComicDict[row[0]] = row[1]
        elif row[1] == 'hero':
            nodeHeroDict[row[0]] = row[1]


print(nodeReader)
print(nodeComicDict)
print(nodeHeroDict)
print("The number of heroes is: ")
print(len(nodeHeroDict))
print("The number of comics is: ")
print(len(nodeComicDict))


edgeHeroesComicDict = collect.defaultdict(list)#collect.OrderedDict()
edgeComicHeroesDict = collect.defaultdict(list)
total = 0
maxi = 0
mini= 1
with open('edges.csv', 'r') as edgefile:
    next(edgefile)
    edgeReaderHC = csv.reader(edgefile, skipinitialspace=True, delimiter=',', quotechar='"')
    for row in edgeReaderHC:
        edgeHeroesComicDict[row[1]].append(row[0])
    for k,v in edgeHeroesComicDict.items():
        if(mini > len(v)):
            mini = len(v)
        if(maxi < len(v)):
            maxi = len(v)
        #print(v)
        total += len(v)
    edgefile.close()

aveHperC = (total/len(edgeHeroesComicDict))

print(edgeHeroesComicDict)
print(len(edgeHeroesComicDict))
print("The mean number of heroes per comic is: ")
print(aveHperC)
print("The minimum number of heroes per comic is: ")
print(mini)
print("The max number of heroes per comic is: ")
print(maxi)

aveHperC = 0
total = 0
maxi = 0
mini= 1

with open('edges.csv', 'r') as edgefile:
    next(edgefile)
    edgeReaderCH = csv.reader(edgefile, skipinitialspace=True, delimiter=',')
    for row in edgeReaderCH:
        edgeComicHeroesDict[row[0]].append(row[1])
    print(edgeComicHeroesDict)
    for k,v in edgeComicHeroesDict.items():
        if(mini > len(v)):
            mini = len(v)
        if(maxi < len(v)):
            maxi = len(v)
        #print(v)
        total += len(v)
    edgefile.close()


aveHperC = (total/len(edgeComicHeroesDict))



print(edgeComicHeroesDict)
print(len(edgeComicHeroesDict))
print("The mean number of comics per hero is: ")
print(aveHperC)
print("The minimum number of comics per hero is: ")
print(mini)
print("The max number of comics per hero is: ")
print(maxi)


total = 0
maxi = 0
mini= 1
heroNetDict = collect.defaultdict(list)

with open('hero-network.csv', 'r') as heroNetfile:
    next(heroNetfile)
    heroNetReader = csv.reader(heroNetfile, delimiter=',', quotechar='"')
    for row in heroNetReader:                          #https://stackoverflow.com/questions/18289678/python-iterating-through-a-dictionary-with-list-values
        if not heroNetDict[row[0]]:
            heroNetDict[row[0]].append(row[1])
        else:
            dictBinarySearchAndInsert(row[0], row[1], heroNetDict)
    heroNetfile.close()
    for k,v in heroNetDict.items():
        if(mini > len(v)):
            mini = len(v)
        if(maxi < len(v)):
            maxi = len(v)
        #print(v)
        total += len(v)



print(heroNetDict["BLACK PANTHER/T'CHAL"])
print(heroNetDict)
aveHperC = (total/len(heroNetDict))

print(len(heroNetDict))
print("The mean number of heroes per hero is: ")
print(aveHperC)
print("The minimum number of heroes per hero is: ")
print(mini)
print("The max number of heroes per hero is: ")
print(maxi)
