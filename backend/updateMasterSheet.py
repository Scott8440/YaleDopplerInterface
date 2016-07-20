# updateMasterSheet.py


import os
import pidly
from datetime import datetime

###############################################################################
#   PID        OBJNM        I2     Mode       OBSNM        DATE    #   Bin    #
# #############################################################################
# struct   #    qbc    #   qbc  #  struct  #  file   #     file    #   sheet  #
###############################################################################


# Look through all directories (2012-2015)
    # Look at all *.dat in the directories
        #for all of the observations in the .dat

        # Date: from the filename
        # OBSNM (Observation number): from filename
        # Restore the logstruct:
            # parse information

# Find the latest date recorded in master.ascii
oldSheet = open('/home/scottsmith/Desktop/CHIRON/master.ascii', 'r')
for line in oldSheet:
    pass
lastDate = line[0:6]
latestYear = int(str("20"+str(lastDate[0:2])))

# Get current year to update the sheet to this year
currentYear = int(str(datetime.now())[0:4])

year = latestYear

os.chdir('/tous/mir7/logstructs/'+str(year))
f = open('/home/scottsmith/Desktop/CHIRON/master2.ascii', 'a')

while (year <= currentYear):

    os.chdir('../'+str(year))
    idl = pidly.IDL()
    print(os.getcwd())

    for struct in os.listdir():                         #Each Day
        date = int(struct[0:6])
        if ((year == latestYear and (int(lastDate) < date)) or
            (year > latestYear)):
            print("struct: " + str(date))

            idl('restore, ' + '\'' +str(struct) + '\'')
            idl("len = size(log, n_elements=1)")
            length = int(idl.len)
            print("date: " + str(date))
            print("length: " + str(length))

            for k in range(length):                         #Each observation

                idl('x = log['+str(k)+'].(0)')
                filename = str(idl.ev('x')).strip()
                nameEnd = filename.find('.')
                obsnm = filename[nameEnd+1:nameEnd+5]
                idl('prop = log['+str(k)+'].(11)')
                propID = str(idl.ev('prop')).strip()

                if (not("Calib" in propID) and not("Calbi11" in propID)):   #Ignore calibration observations
                    idl('object = log['+str(k)+'].(9)')
                    idl('mode = log['+str(k)+'].DECKER')
                    idl('iod = log['+str(k)+'].IODCELL')
                    idl('bin = log['+str(k)+'].CCDSUM')

                    obj = str(idl.ev('object')).strip()
                    mode = str(idl.ev('mode')).strip()
                    iod = str(idl.ev('iod')).strip()
                    binSize = str(idl.ev('bin')).strip()
                    binSize = binSize[0] + "x" + binSize[2]

                    line = (str(date).ljust(10) + str(obsnm).ljust(10) + \
                            str(propID).ljust(10) + str(obj).ljust(25) + \
                            str(iod).ljust(10) + str(mode).ljust(15) +
                            str(binSize).ljust(10))
                    f.write(line+"\n")
    year += 1

idl.close()
f.close()
