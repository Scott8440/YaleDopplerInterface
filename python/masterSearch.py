# masterSearch.py

# This program searches the file master.ascii (created by masterList.py) and
# returns observation numbers which match the given arguments. This search
# function was written for the CHIRON doppler interface, and only supports
# a few combinations of parameters. These are described below. The program
# outputs a list of observations in a list called observationList, which makes
# this modular to do other operations on the list. The function
# outputList prints out the observations in the form of HTML option tags in
# order to create a selectable list in the CHIRON doppler interface.


##############################################################
#  Date #  OBSNM #  PROPID #  Object #  IOD # MODE #   BIN  #
# ############################################################
#   10  #   10   #   10    #   25   #  10  #  15  #    10  #
##############################################################
#  0-9      10-19    20-29    30-54   55-64  65-79    80-89

import os
import sys

fileLocation = "C:\\xampp\\htdocs\\YaleDoppler\\python\\master.ascii"
#fileLocation = "/home/scottsmith/Desktop/CHIRON/master.ascii"
# returns a list of all unique PIDs in the master.ascii file
def findAllpIDs():
    f = open(fileLocation, 'r')

    IdList = []
    for line in f:
        Id = line[20:29].strip()
        if (Id not in IdList):
            IdList.append(Id)
    return(IdList)

def checkPid(pID):
    val = (pID in findAllpIDs())
    return val

def filterByDate(obsList, date):
    filteredList = []
    for i in range(len(obsList)):
        if (obsList[i][0:6] == date):
            filteredList.append(obsList[i])
    return filteredList

def filterByPid(obsList, pID):
    filteredList = []
    for i in range(len(obsList)):
        if (obsList[i][20:29].strip() == str(pID)):
            filteredList.append(obsList[i])
    return filteredList

def filterByObject(obsList, obj):
    filteredList = []
    for i in range(len(obsList)):
        if (obsList[i][30:54].strip() == obj):
            filteredList.append(obsList[i])
    return filteredList

def filterByIod(obsList, iod):
    filteredList = []
    for i in range(len(obsList)):
        sheetIOD = obsList[i][55:64].strip()
        if (iod == 'OUT' and (sheetIOD == 'OUT' or sheetIOD == '0')):
            filteredList.append(obsList[i])
        elif (iod == 'IN' and (sheetIOD == 'IN')):
            filteredList.append(obsList[i])
    return filteredList

def filterByMode(obsList, mode):
    filteredList = []
    for i in range(len(obsList)):
        if (obsList[i][65:79].strip() == mode):
            filteredList.append(obsList[i])
    return filteredList

def filterByBin(obsList, bins):
    filteredList = []
    for i in range(len(obsList)):
        if (obsList[i][80:89].strip() == bins):
            filteredList.append(obsList[i])
    return filteredList

def initializeAll():
    f = open(fileLocation, 'r')
    observationList = []
    count = 0

    for line in f:
        if (line[0].isnumeric()):                   #skips the title lines
            # date = line[0:6]
            # obsnm = line[10:19].strip()
            # observation = date+'.'+obsnm
            observationList.append(line)
            count += 1
    return observationList

def convertToObs(lst):
    newList = []
    for i in range(len(lst)):
        date = lst[i][0:6]
        obsnm = lst[i][10:19].strip()
        observation = date+"."+obsnm
        newList.append(observation)
    return newList


# prints out a list in the form of HTML tags to create a selectable list
def outputList(obsList):
    if (len(obsList) == 0):
        print("<option disabled>No Matching Observations</option>")
    else:
        print("<option></option>")
        for i in obsList:
            print("<option value="+str(i)+">"+str(i)+"</option>")

# Arguments:
# -p    PID
# -d    date
# -m    mode
# -b    bin
# -i    iodine
# -o    object

# the argument that follows the -? argument is the parameter that matches that
# argument. For example, masterSearch.py -p 308 -i IN finds all observations
# for PID 308 with the iodine IN


nArgs = len(sys.argv)
observationList = initializeAll()
output = True
for i in range(nArgs):
    curArg = sys.argv[i]
    print(curArg)
    if (i % 1 == 0):            #argument is odd so it is a -? argument
        if (curArg == '-p'):
            observationList = filterByPid(observationList, sys.argv[i+1])
        elif (curArg == '-d'):
            observationList = filterByDate(observationList, sys.argv[i+1])
        elif (curArg == '-m'):
            observationList = filterByMode(observationList, sys.argv[i+1])
        elif (curArg == '-b'):
            observationList = filterByBin(observationList, sys.argv[i+1])
        elif (curArg == '-i'):
            observationList = filterByIod(observationList, sys.argv[i+1])
        elif (curArg == '-o'):
            observationList = filterByObject(observationList, sys.argv[i+1])
        elif (curArg == '-pidCheck'):
            output = False
            print(checkPid(sys.argv[i+1]))
        else:
            pass
if (output):
    outputList(convertToObs(observationList))







#extra space
