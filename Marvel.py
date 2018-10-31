import csv
import collections as collect



heroDict = collect.OrderedDict()
comicDict = collect.OrderedDict()
#https://docs.python.org/3.7/library/csv.html
with open('nodes.csv', 'r') as nodefile:
    next(nodefile)
    nodeReader = csv.reader(nodefile, skipinitialspace=True, delimiter=',', quotechar='"')
    for row in nodeReader:
        if row[1] == 'comic':
            comicDict[row[0]] = row[1]
        elif row[1] == 'hero':
            heroDict[row[0]] = row[1]

print(nodeReader)
print(comicDict)
print(heroDict)
print("The number of heroes is: ")
print(len(heroDict))
print("The number of comics is: ")
print(len(comicDict))
