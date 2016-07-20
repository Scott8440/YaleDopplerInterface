#iodineCheck.py

from astropy.io import fits

f = open('/home/scottsmith/Desktop/CHIRON/iodineDiff.ascii', 'r')

badCount = goodCount = 0
for line in f:
    dot = line.find('.')
    date = line[dot-6:dot]
    num  = line[dot+1:dot+5]

    try:
        file = fits.open("/tous/mir7/fitspec/"+date+"/achi"+date+"."+num+".fits")
        print(line[:-1] + "\tGOOD")
        goodCount += 1
    except:
        #print(line[:-1] + "\tBAD")
        #badCount += 1
        pass


print("Good: " + str(goodCount))
print("Bad:  " + str(badCount))
