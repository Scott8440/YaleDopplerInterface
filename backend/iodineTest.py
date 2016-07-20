# /tous/mir7/fitspec/121124

#Example 120218.1589
#Example 120312.fits
#Example 120323.1144-1158

#120723.1120 has the iodine in
#120723.1153 has no iodine

#120725.1117 has iodine

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import time

while (True):
    name = str(input("Observation Date: "))
    if (name == 'quit'):
        break
    num  = str(input("Observation Number: "))
    print("/tous/mir7/fitspec/"+name+"/achi"+name+"."+num+".fits")
    try:
        file = fits.open("/tous/mir7/fitspec/"+name+"/achi"+name+"."+num+".fits")
    except:
        print("No file exists")
        continue

    x_axis = []
    y_axis = []

    scidata = file[0].data
    cols = file[0]
    print(len(scidata))
    print(scidata.shape)

    for i in range(10,30):
        x_axis = []
        y_axis = []
        for j in range(3200):
             x_axis.append((scidata[i][j][0]))
             y_axis.append((scidata[i][j][1]))

        plt.plot(x_axis, y_axis)
        plt.title("Chunk Number: " + str(i))
        plt.show()
