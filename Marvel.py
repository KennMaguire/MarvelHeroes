import csv
import collections as collect



nodeHeroDict = {}#collect.OrderedDict()
nodeComicDict = {}#collect.OrderedDict()
#https://docs.python.org/3.7/library/csv.html
with open('nodes.csv', 'r') as nodefile:
    next(nodefile)
    nodeReader = csv.reader(nodefile, skipinitialspace=True, delimiter=',', quotechar='"')
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
        if(min > len(v)):
            min = len(v)
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
    edgeReaderCH = csv.reader(edgefile, skipinitialspace=True, delimiter=',', quotechar='"')
    for row in edgeReaderCH:
        edgeComicHeroesDict[row[0]].append(row[1])
    print(edgeComicHeroesDict)
    for k,v in edgeComicHeroesDict.items():
        if(min > len(v)):
            min = len(v)
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
