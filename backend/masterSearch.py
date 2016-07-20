# masterSearch.py

# This program searches the file master.ascii (created by masterList.py) and
# returns observation numbers which match the given arguments. This search
# function was written for the CHIRON doppler interface, and only supports
# a few combinations of parameters. These are described below. The program
# outputs a list of observations in a list called observationList, which makes
# this pretty modular to do other operations on the list. The function
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

# returns a list of all unique PIDs in the master.ascii file
def findAllpIDs():
    f = open('/home/scottsmith/Desktop/CHIRON/master.ascii', 'r')

    IdList = []
    for line in f:
        Id = line[20:29].strip()
        if (Id not in IdList):
            IdList.append(Id)
    return(IdList)

#returns all observations of a certain object from a PID
def findObjfromPID(obj, pID):
    f = open('/home/scottsmith/Desktop/CHIRON/master.ascii', 'r')

    count = 0
    Id = str(pID)
    obj = str(obj)
    observationList = []

    for line in f:
        if (line[20:29].strip() == Id):
            if (line[30:54].strip() == obj):
                date = line[0:6]
                obsnm = line[10:19].strip()
                observation = date+'.'+obsnm
                print(line)
                observationList.append(observation)
                count += 1
    return observationList

def iodineSearch(mode, date):

    f = open('/home/scottsmith/Desktop/CHIRON/master.ascii', 'r')
    observationList = []
    print(str(date))
    for line in f:
        if (line[0:6].strip() == str(date)   and
           (line[30:54].strip() == 'iodine') and
           (line[65:79].strip() == str(mode))):
           obsnm = line[10:19].strip()
           obs = date + "." + osbnm
           observationList.append(obs)
    return observationList

# Searches through master.ascii with an arbitrary number of arguments (1-6) and
# returns all observations which match every argument
def masterSearch(*args):

    # python masterSearch.py type [PID [Object [Iodine [Mode [Bin]]]]] [Mode Date]
    #   type: (M|I)
    #           M, master search
    #           I, iodine Search, only takes mode and date
    #   PID
    #   Object
    #   Iodine: ('IN'|'OUT')
    #   Mode:   ('slit'|'narrow_slit'|'fiber'|'slicer')
    #   Bin:    (MxN) where M and N are integers from 1:4

    f = open('/home/scottsmith/Desktop/CHIRON/master.ascii', 'r')
    observationList = []
    count = 0
    numArgs = len(args)

    #SET UP ARGUMENT VARIABLES
    if (numArgs > 0):                   #PID
        pid = str(args[0]).strip()
        idLength = len(pid)
    if (numArgs > 1):                   #Object
        obj = str(args[1]).strip()
        objLength = len(str(obj))
    if (numArgs > 2):                   #Iodine
        iod = str(args[2]).strip()
    if (numArgs > 3):                   #Mode
            mode = str(args[3]).strip()
    if (numArgs > 4):                   #Bin
            bins = str(args[4]).strip()

    for line in f:
        if (line[20:29].strip() == pid):                                       #get the PID
            date = line[0:6]
            obsnm = line[10:19].strip()
            observation = date+'.'+obsnm
            if (numArgs > 1):                                                   #If observation
                if (line[30:54].strip() == obj):                                #check if the object is the same
                    lineObj = line[30:49].strip()
                    if (lineObj == obj):
                        if (numArgs > 2):                                       #if iodine
                            lineIOD = line[50:59].strip()
                            if ((iod == 'IN' and lineIOD == 'IN') or            #check if the iodine is the same
                                (iod == 'OUT' and (lineIOD == 'OUT' or lineIOD == '0'))):
                                    if (numArgs > 3):                           #if Mode
                                        lineMode = line[65:79].strip()
                                        if (lineMode == mode):
                                            if (numArgs > 4):                   #if Bin
                                                lineBin = line[80:89].strip()
                                                if (lineBin == bins):           #check if bins is the same
                                                    observationList.append(observation)
                                                    print(line, end="")
                                                    count += 1
                                            else:
                                                #only 4
                                                observationList.append(observation)
                                                print(line, end="")
                                                count += 1
                                    else:
                                        #only 3
                                        observationList.append(observation)
                                        print(line, end="")
                                        count += 1
                        else:
                           #only 2
                           observationList.append(observation)
                           print(line, end="")
                           count += 1
            else:
                #only 1
                observationList.append(observation)
                print(line, end="")
                count += 1
    print(count)
    return observationList

def filterByDate(obsList, date):
    filteredList = []
    for i in range(len(obsList)):
        if (obsList[i][0:6] == date):
            filteredList.append(obsList[i])
    return filteredList

def filterByPid(obsList, pID):
    print(pID)
    filteredList = []
    for i in range(len(obsList)):
        #print(obsList[i][20:29])
        if (obsList[i][20:29].strip() == str(pID)):
            #print(obsList[i])
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
        if (iod == 'IN' and (sheetIOD == 'OUT' or sheetIOD == '0')
            or iod == 'OUT' and (sheetIOD == 'IN')):
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
    f = open('/home/scottsmith/Desktop/CHIRON/master.ascii', 'r')
    observationList = []
    count = 0

    for line in f:
        if (line[0].isnumeric()):                   #skips the title lines
            # date = line[0:6]
            # obsnm = line[10:19].strip()
            # observation = date+'.'+obsnm
            observationList.append(line)
            count += 1
    print(count)
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
    for i in obsList:
        print("<option value="+str(i)+">"+str(i)+"</option>")


# Main
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
print("Args: " + str(nArgs))
for i in range(nArgs):
    curArg = sys.argv[i]
    print(str(i) + ": " + str(curArg))
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
#print(convertToObs(observationList))
outputList(convertToObs(observationList))
print(len(observationList))

#
# nArgs = len(sys.argv)
# if (sys.argv[1] == 'M'):
#     if (nArgs == 3):
#         masterSearch(sys.argv[2])
#     elif (nArgs == 4):
#         masterSearch(sys.argv[2], sys.argv[3])
#     elif (nArgs == 5):
#         masterSearch(sys.argv[2], sys.argv[3], sys.argv[4])
#     elif (nArgs == 6):
#         masterSearch(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
#     elif (nArgs == 7):
#         masterSearch(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
#     else:
#         pass
#
# elif (sys.argv[1] == 'I'):
#     iodineSearch(sys.argv[2], sys.argv[3])
#















#extra space
