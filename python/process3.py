# process3.py

import smtplib

fromaddr = 'scott8440@gmail.com'
toaddrs  = 'scott.smith@yale.edu'
SUBJECT  = "Test Subject"
TEXT     = "Test Text"
msg      = 'Subject: %s\n\n%s' % (SUBJECT, TEXT)


# Credentials (if needed)
username = 'scott8440'
password = 'brock3592'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
