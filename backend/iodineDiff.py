# iodineDiff.py

# Iterates through all of the logstructs and logsheets from 2012-2016 and prints
# the observations where the iodine differs from the logsheet and logstructs
# For example, the logsheet could say 'y' and the logstruct could say 'OUT'
import os
import pidly


os.chdir('/tous/mir7/logstructs/2012')

year = 2012
f = open('/home/scottsmith/Desktop/CHIRON/iodineDiff2.ascii', 'w')
for i in range(5):

    os.chdir('../'+str(year+i))
    idl = pidly.IDL()
    print(os.getcwd())
    f.write("Date".ljust(10) + "OBSNM".ljust(10) + "PropID".ljust(10) + "Object".ljust(20) + "Iodine".ljust(10) + "Mode".ljust(15) + "Bin".ljust(10))
    for struct in os.listdir():                         #Each Day
        idl('restore, ' + '\'' +str(struct) + '\'')

        idl("len = size(log, n_elements=1)")
        length = int(idl.len)

        date = struct[0:6]
        print("date: " + str(date))


        for k in range(length):                         #Each observation

            idl('x = log['+str(k)+'].(0)')
            filename = str(idl.x)
            nameEnd = filename.find('.')
            obsnm = filename[nameEnd+1:nameEnd+5]

            idl('prop = log['+str(k)+'].(11)')
            propID = str(idl.ev('prop')).strip()

            try:
                sheet = open('/tous/mir7/logsheets/'+str(year+i)+'/'+str(date)+'.log')
                lineNum = -1
                for line in sheet:
                    lineNum += 1
                    if (lineNum >= 9):
                        numEndS = line.find(' ', 3)
                        numEndT = line.find('\t', 3)

                        sheetObsnm = line[0:numEndS].strip()
                        #print("obsnm: " + str(sheetObsnm))
                        if (line[0] != '-' and '-' in sheetObsnm):

                            first  = int(sheetObsnm[sheetObsnm.find('-')-4:sheetObsnm.find('-')])
                            second = int(sheetObsnm[sheetObsnm.find('-')+1:sheetObsnm.find('-')+5])
                            if (obsnm.isdigit() and int(obsnm) <= second and int(obsnm) >= first):
                                bins = line[52:57].strip()
                                #print(line)
                                #bins are 53 to 56
                        elif (sheetObsnm == str(obsnm)):
                            bins = line[52:57].strip()
                            sheetIOD = line[25:28].strip()


                if (not("Calib" in propID) and not("Calbi11" in propID)):

                    print(sheetIOD, end=", ")

                    idl('object = log['+str(k)+'].(9)')
                    idl('mode = log['+str(k)+'].DECKER')
                    idl('iod = log['+str(k)+'].IODCELL')

                    obj = str(idl.ev('object')).strip()
                    mode = str(idl.ev('mode')).strip()
                    iod = str(idl.ev('iod')).strip()

                    line = str(date).ljust(10) + str(obsnm).ljust(10) + str(propID).ljust(10) + str(obj).ljust(20) + str(iod).ljust(10) + str(mode).ljust(15) +str(bins).ljust(10)
                    # f.write(line+"\n")
                    # print(str(iod), end="")

                    if (sheetIOD == 'y' and (str(iod) == 'OUT' or str(iod) == '0') or (sheetIOD == 'n' and (str(iod) == 'IN'))):
                        f.write(str(sheetIOD) + ", " + str(iod) + ", " + str(date) + "."+str(obsnm)+", "+str(obj)+"\n")
            except:
                noSheet = True
                bins = "None"
                if (not("Calib" in propID) and not("Calbi11" in propID)):
                    idl('object = log['+str(k)+'].(9)')
                    idl('mode = log['+str(k)+'].DECKER')
                    idl('iod = log['+str(k)+'].IODCELL')

                    obj = str(idl.ev('object')).strip()
                    mode = str(idl.ev('mode')).strip()
                    iod = str(idl.ev('iod')).strip()

                    line = str(date).ljust(10) + str(obsnm).ljust(10) + str(propID).ljust(10) + str(obj).ljust(20) + str(iod).ljust(10) + str(mode).ljust(15) +str(bins).ljust(10)
                    # f.write(line+"\n")
                    #print()

idl.close()
f.close()
