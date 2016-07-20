#iodineFix.py


f = open('/home/scottsmith/Desktop/CHIRON/iodineDiff.ascii', 'r')
new = open('/home/scottsmith/Desktop/CHIRON/iodineDiff2.ascii', 'w')
for line in f:
    for i in line:
        if (i == 'y'):
            print("\ny", end="")
            new.write("\ny")
        elif (i == 'n'):
            print("\nn", end="")
            new.write("\nn")
        else:
            print(i, end="")
            new.write(i)
