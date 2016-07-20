#objectCheck.py


f = open('/home/scottsmith/Desktop/CHIRON/master3.ascii', 'r')

for line in f:
    if (len(line) != 91):
        print(line)
