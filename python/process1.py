# process1.py

import smtplib
import sys

print("called")
# ("python process1.py .$email .$file1Arr .$file2Arr .$file3Arr .$dop1Arr .$dop2Arr")
# file1str = str(sys.argv[2])
# file2str = str(sys.argv[3])
# file3str = str(sys.argv[4])
# dop1file = str(sys.argv[5])
# dop2Arr  = str(sys.argv[6])

fromaddr = 'scott8440@gmail.com'
#input for email
toaddrs  = str(input("toaddrs: "))
#input for file1
file1str = str(input("file name: "))
#input for file2
file2str = str(input("file name: "))
#input for file3
file3str = str(input("file name: "))
#input for dop1File
dop1str = str(input("file name: "))
#input for dop2File
dop2str = str(input("file name: "))
#input for tag
tag = str(input("tag: "))

msg  = ("file 1: " + file1str + "\n")
msg += ("file 2: " + file2str + "\n")
msg += ("file 3: " + file3str + "\n")
msg += ("dop file 1: " + dop1str + "\n")
msg += ("dop file 2: " + dop2str + "\n")
print(msg)

# Credentials (if needed)
username = 'chironinterface'
password = 'dopplercode2016'

# The actual mail send
print(toaddrs)
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

quit()
