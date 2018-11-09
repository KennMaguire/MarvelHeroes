#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import csv
import collections as collect


def dictBinarySearchAndInsert(key, val, _unsortedDict):   #https://www.geeksforgeeks.org/binary-search/ (used for reference)
    _unsortedDict[key].sort()
    low = 0
    hi = len(_unsortedDict[key])-1
    while low <= hi:
        mid = int(low + (hi-low)/2)         #get the midpoint
        if val == _unsortedDict[key][mid]:  #if found, return
            return
        elif val < _unsortedDict[key][mid]:
            hi = mid-1
        elif val > _unsortedDict[key][mid]:
            low = mid + 1

    _unsortedDict[key].append(val)          #if not found, add partner to the list at the specified key value


nodeHeroDict = {}#collect.OrderedDict()
nodeComicDict = {}#collect.OrderedDict()
#https://docs.python.org/3.7/library/csv.html
with open('nodes.csv', 'r') as nodefile:                #open node file for reading
    next(nodefile)                                      #skip first line in file
    nodeReader = csv.reader(nodefile, delimiter=',')
    for row in nodeReader:                              #get each row from the nodeReader (list of rows in )
        if row[1] == 'comic':                           #if value found is a comic, add to the dict with name as key and value as comic
            nodeComicDict[row[0]] = row[1]
        elif row[1] == 'hero':                          #if value found is a hero, add to the dict with name as key and value as hero
            nodeHeroDict[row[0]] = row[1]


#print(nodeReader)
#print(nodeComicDict)
#print(nodeHeroDict)
print("The number of heroes is: ")
print(len(nodeHeroDict))
print("The number of comics is: ")
print(len(nodeComicDict))


edgeHeroesComicDict = collect.defaultdict(list)
edgeComicHeroesDict = collect.defaultdict(list) #create two dictionaries of lists
total = 0
maxi = 0                                        #reset values
mini= 1
with open('edges.csv', 'r') as edgefile:
    next(edgefile)                              #skip first line in edge file
    edgeReaderHC = csv.reader(edgefile, skipinitialspace=True, delimiter=',', quotechar='"')
    for row in edgeReaderHC:
        edgeHeroesComicDict[row[1]].append(row[0])  # append hero value to list for each comic key
    for k,v in edgeHeroesComicDict.items():         #iterate through dict for each key and value (list)
        if(mini > len(v)):                          #if length of list of heroes is less than min, set to value of length
            mini = len(v)
        if(maxi < len(v)):                          #if length of list of heroes is greater than max, set to value of length
            maxi = len(v)
        #print(v)
        total += len(v)                             #add length of list to total
    edgefile.close()

ave = (total/len(edgeHeroesComicDict))              #get average number of heroes per comic by dividing total number of heroes by number of comic

#print(edgeHeroesComicDict)
#print(len(edgeHeroesComicDict))
print("The mean number of heroes per comic is: ")
print(ave)
print("The minimum number of heroes per comic is: ")
print(mini)
print("The max number of heroes per comic is: ")
print(maxi)

ave = 0
total = 0                                          #reset values
maxi = 0
mini= 1

with open('edges.csv', 'r') as edgefile:
    next(edgefile)
    edgeReaderCH = csv.reader(edgefile, skipinitialspace=True, delimiter=',')
    for row in edgeReaderCH:
        edgeComicHeroesDict[row[0]].append(row[1])    #append each comic value to list for each hero key
    #rint(edgeComicHeroesDict)
    for k,v in edgeComicHeroesDict.items():           #iterate through dict for each key and value (list0)
        if(mini > len(v)):                            #if length of list of comics is less than min, set to value of length
            mini = len(v)
        if(maxi < len(v)):                            #if length of list of comics is greater than mamx, set to value of length
            maxi = len(v)
        #print(v)
        total += len(v)                               #add length of list to total
    edgefile.close()


ave = (total/len(edgeComicHeroesDict))               #get average number of comics per hero by dividing total number of comics by number of heroes



#print(edgeComicHeroesDict)
#print(len(edgeComicHeroesDict))
print("The mean number of comics per hero is: ")
print(ave)
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
        if not heroNetDict[row[0]]:                    #if list is empty for specifed key (hero 1), append value to list (hero 2)
            heroNetDict[row[0]].append(row[1])
        else:
            dictBinarySearchAndInsert(row[0], row[1], heroNetDict)  #(search for value (hero 2), in list at the specified key in the dictionary, if found, insert)
    heroNetfile.close()
    for k,v in heroNetDict.items():
        if(mini > len(v)):                             #if length of list of heroes is less than min, set to value of length
            mini = len(v)
        if(maxi < len(v)):                             #if length of list of heroes is greater than max, set to value of length
            maxi = len(v)
        #print(v)
        total += len(v)                                #add length of list to total



#print(heroNetDict["BLACK PANTHER/T'CHAL"])
#print(heroNetDict)
ave = (total/len(heroNetDict))                         #get average number of partners per hero by dividing total number of partners per hero

#print(len(heroNetDict))
print("The mean number of heroes per hero is: ")
print(ave)
print("The minimum number of heroes per hero is: ")
print(mini)
print("The max number of heroes per hero is: ")
print(maxi)
