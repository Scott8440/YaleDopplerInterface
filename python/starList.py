#starList.py

import sys

def findObjects(pID):
    f = open('C:\\Users\\Scott\\Desktop\\CHIRON\\MasterLists\\master.ascii', 'r')
    #PID starts at 30
    #goes for length of PID
    objectList = []
    count = 0
    Id = str(pID)
    length = len(Id)
    if (length == 0):                    #No PID
        for line in f:
            if (line[20] == ' '):
                #print(line)
                count += 1
    else:
        for line in f:
            if (line[20:20+length] == Id):
                lineObj = line[30:49].strip()
                if (lineObj not in objectList):
                    objectList.append(lineObj)
                 #print(line)
                    count += 1
    outputList(objectList)

    # print("Total: " + str(count))
    # print(objectList)

def outputList(obsList):
    for i in obsList:
        # print(str(i))
        print("<option value="+ "\"" +str(i) + "\"" + ">"+str(i)+"</option>")

findObjects(sys.argv[1])
