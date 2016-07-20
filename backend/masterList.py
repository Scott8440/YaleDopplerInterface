# Master Sheet Creator

# This program will create an ascii file which includes the information shown
# in the table below for all of the logstructs from 2012 to 2016. The info is
# written to a text file specified in the line f = open(...
# This program takes several hours to run because it has to restore every log
# struct one at a time. For this reason, it is best to run this ONLY if absolutely
# necessary. Otherwise, use updateMasterSheet.py, which will append the information
# onto the specified file.
# Pidly is used to interact with IDL and is included in the anaconda distribution,
# and can also be installed with pip.

import os
import pidly
from datetime import datetime


###############################################################################
#   PID        OBJNM        I2     Mode       OBSNM        DATE    #   Bin
# #############################################################################
# struct   #    qbc    #   qbc  #  struct  #  file   #     file    #   sheet
###############################################################################


# Look through all directories (2012-2015)
    # Look at all *.dat in the directories
        #for all of the observations in the .dat

        # Date: from the filename
        # OBSNM (Observation number): from filename
        # Restore the logstruct:
            # parse information


year = 2012                              # Change this to adjust starting year
currentYear = int(str(datetime.now())[0:4])

os.chdir('/tous/mir7/logstructs/'+str(year))
f = open('/home/scottsmith/Desktop/CHIRON/master2.ascii', 'w')
while (year <= currentYear):

    os.chdir('../'+str(year+i))
    idl = pidly.IDL()
    print(os.getcwd())
    f.write("Date".ljust(10) + "OBSNM".ljust(10) + "PropID".ljust(10) +
            "Object".ljust(25) + "Iodine".ljust(10) + "Mode".ljust(15) + "Bin".ljust(10))

    for struct in os.listdir():                         #Each Day

        idl('restore, ' + '\'' +str(struct) + '\'')
        idl("len = size(log, n_elements=1)")
        length = int(idl.len)
        date = struct[0:6]
        print("date: " + str(date))

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

                line = str(date).ljust(10) + str(obsnm).ljust(10) + str(propID).ljust(10) +
                       str(obj).ljust(25) + str(iod).ljust(10) + str(mode).ljust(15) + str(binSize).ljust(10)

                f.write(line+"\n")
    year += 1
idl.close()
f.close()
