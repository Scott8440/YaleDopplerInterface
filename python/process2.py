# process2.py

import smtplib

fromaddr = 'scott8440@gmail.com'
toaddrs  = 'scott.smith@yale.edu'
msg = 'Test message from process2.py'


# Credentials (if needed)
username = 'scott8440'
password = 'brock3592'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
