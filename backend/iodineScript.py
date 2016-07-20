# iodineScript.py

import os
import pidly
import sys

os.chdir('/home/scottsmith/Desktop/CHIRON/dop_old')

idl = pidly.IDL()

year = sys.argv[1]

for i in range (1,13):
    x = ("%02d" % i)
    yrmo = str(year) + x
    if (int(yrmo) >= 1207):
        print(yrmo)

        idl.pro('vdiodbatch', yrmo=yrmo, mode='narrow_slit')
