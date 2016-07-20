#adjustFormatting.py


f = open('/home/scottsmith/Desktop/CHIRON/master2.ascii', 'r')
new = open('/home/scottsmith/Desktop/CHIRON/master3.ascii', 'w')
badList = []

for line in f:
    data = line.split()    # Splits on whitespace
    if (len(data) == 7):
        newLine = ('{0[0]:<10}{0[1]:<10}{0[2]:<10}{0[3]:<25}{0[4]:<10}{0[5]:<15}{0[6]:<10}'.format(data))
        new.write(newLine + "\n")
    elif (len(data) == 5):
        badList.append(data)
        new.write(newLine + "\n")
    elif (len(data[3]) <= 20):
        #print(line)
        newLine = line[:50] + '     ' + line[50:]
        #print(newLine)
        new.write(newLine)

    if (len(data[3]) > 20):
        #print(data)
        obj = data[3]
        # print(obj)
        if ("OUT" in obj):
            start = obj.find("OUT")
        else:
            start = obj.find("IN")
        # print(obj[start:])
        end = obj[start:]
        obj = obj[:start]
        date = data[0]
        obsnm = data[1]
        pid = data[2]
        #obj
        #end
        mode = data[4]
        bins = data[5]
        newLine = str(date).ljust(10) + str(obsnm).ljust(10) + str(pid).ljust(10) + str(obj).ljust(25) + str(end).ljust(10) + str(mode).ljust(15) +str(bins).ljust(10)
        new.write(newLine + "\n")

print(badList)

# [0]   10
# [1]   10
# [2]   10
# [3]   25
# [4]   10
# [5]   15
# [6]   10
