#objectCheck.py



iods = open('/home/scottsmith/Desktop/CHIRON/iodineDiff.ascii', 'r')

#starts at 8
for oldLine in iods:
    date = oldLine[8:14]
    num = oldLine[15:19]
    print(date + " " + num)

    f = open('/home/scottsmith/Desktop/CHIRON/master.ascii', 'r')

    for line in f:
        if (line[0:6] == date and line[10:14] == num):
            print(line, end = "")
