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

total = 0
with open('edges.csv', 'r') as edgefile:
    next(edgefile)
    edgeReader = csv.reader(edgefile, skipinitialspace=True, delimiter=',', quotechar='"')
    for row in edgeReader:
        edgeHeroesComicDict[row[1]].append(row[0])
    for k,v in edgeHeroesComicDict.items():
        print(v)
        total += len(v)



aveHperC = (total/len(edgeHeroesComicDict))



print(edgeHeroesComicDict)
print(len(edgeHeroesComicDict))
print("The average number of heroes per comic is: ")
print(aveHperC)
