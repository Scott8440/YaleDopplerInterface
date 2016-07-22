#skeleton.py

# This program shows how to take all the information given from the website and
# run the whole process.

import os
import pidly
import sys
#for email:
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


# Collect input of metadata from webpage. Must know exactly how data is sent in
# and especially what order it is sent in. Input must be ended with a newline

#input 1 - oldDSST
oldDSST = str(input())
if (oldDSST == 'true'):
    oldDSST = True
else:
    oldDSST = False
#input 2 - toAddrs
toaddrs  = str(input())
#input 3 - pID
pID      = str(input())
#input 4 - starName
starName = str(input())
# ****** DSST INPUTS
if (oldDSST == False):
    #input 5
    dsstTemplate = str(input())               # obsnm for making dsst
    #input 6
    dsstBstars = str(input())                 # B-star for the dsst

    templateArr  = dsstTemplate.split(' ')    # array of the DSST template observations
    tempDate = str(templateArr[0][0:6])       # extract the date for template obs
    iodineArray = dsstBstars.split(' ')
# ***** Doppler INPUTS
#input 7
dopplerObs  = str(input())            # obs for running the program
dopplerArray = dopplerObs.split(' ')
#input 8
#dopplerIodines  = str(input())        # iodine or b-star for program

tag  = idToTag(pID)
dateArray = makeDateArray(dopplerArray)
interfaceBccor = str(findBccor(templateArr))
fileDirectory    = '/tous/mir7/files/'
outfileDirectory = '/tous/mir7/interface/'

# Use this to get an array of non-repeating dates that make up the program obs
# This is used in reduce.pro through dr_run.pro
def makeDateArray(progObs):
    dateArray = []
    for obs in progObs:
        date = obs[0:6]
        dateArray.append(date)
    dateArray = sorted(list(set(dateArray)))
    return dateArray

# Uses the template observation array to find the barycentric correction of the
# middle observation
def findBccor(tempArr):
    midObs = tempArr[len(tempArr)/2]

    idl = pidly.IDL()
    idl('restore, \'/tous/mir7/bary/qbcvel.dat\'')
    idl('x = where(strmid(bcat.obsnm, 10, 11, /reverse_offset) eq '+ midObs + ')')
    idl('bccor = bcat[x].bc')
    bccor = idl.ev('bccor')
    idl.close()
    return bccor

# Converts pID to the corresponding tag (Just adds an 'i' after the pID)
def idToTag(pID):
    tag = pID+'i'
    return tag

#TODO: combine the right observations into variable called interfaceArr

# How to use IDL

# initialize the idl object with:
# idl = pidly.IDL()

# Example with running iodine
# Run a procedure with idl.pro(). Can use python variables in the argument list
# date = ""
# idl.pro('vdiodbatch', date=date, mode='slit')
# The python script will resume once the idl procedure is complete
# FYI The same standard output is used
# in order to access idl structures and variables, use idl.ev()
# example: assume there is a variable called vd in this idl environment
# pythonVD = idl.ev('vd')

#TODO: Check to make sure there are a good number of output files
#TODO: Vanking
#TODO: CHECK CFNEW STUFF


os.chdir("/home/scottsmith/Desktop/CHIRON/fischer-dop1/dop1")
idl = pidly.IDL()

if (oldDSST == False):
    #Create a DSST and then run the observations with that DSST
    #clean the template observations
    idl.obsnm = dsstTemplate
    idl('dopenv = ctio4k_init('+ templateArr[0] +', \'junk\', 0.0, \
         iss_obnm=\'junk\', date=\''+ tempDate +'\', tag='+ tag')')
    idl('dop_rayclean, obsnm, dopenv=dopenv, observatory=\'ctio4k\', \
         obstack=obstack, star=star, mdtck=5.0, /auto')
    idl('save, star, f=\'/tous/mir7/files/hd'+ starName + tag +'_achi' + tempDate + '.dat')

    # make the iodine observations for the dsst
    idl('cd, "/home/scottsmith/Desktop/CHIRON/dop_old_interface"')
    idl.interfaceArr = iodineArray
    idl('vdiodbatch, date=\'' + tempDate + '\', mode=\'narrow_slit\', \
         interfaceArr=interfaceArr, outputFiles=outputFiles, tag='+tag)
    outputFiles = idl.ev('outputFiles')
    #outputFiles are sent to make_dsst as iodArr

    # Make the dsst
    dsstnm = 'dsst' + starName + tag + 'chi' + date + '.dat'
    outfile = outfileDirectory + pId + 'dsst' + starName + tag + 'chi' + date + '.dat'
    idl('cd, "/home/scottsmith/Desktop/CHIRON/fischer-dop1/dop1/z_iss_jj"')
    idl('specin=star')
    idl('make_dsst, \''+ starName +'\', \''+ tag +'\', \'chi'+ tempDate +'\', \
        specin=specin, ngrid=30, /mov, /ctio4k, outfile=\''+ outfile +'\', iodArr=outputFiles')
    # Now outfile contains a newly created DSST for this star

    # If new DSST was created:
    idl('cd, "/home/scottsmith/Desktop/CHIRON/dop_old"')
    idl.obsArr = dopplerArray
    idl.dateArr = dateArray
    idl('dr_run, star=\'' +starName+ '\', tag=\'' +tag+ '\', /interface, \
         obsArr=obsArr, dateArr=dateArr, interfaceDSST='+ dsstnm + ', \
         interfaceBccor='+ interfaceBccor +', vdOut=vdOut')
    runOutput = idl.ev('vdOut')

else:       #else just use the old dsst and run the observations
    # If using old DSST:
    idl('cd, "/home/scottsmith/Desktop/CHIRON/dop_old"')
    idl.obsArr = dopplerArray
    idl.dateArr = dateArray
    idl('dr_run, star=\''+ starName +'\', tag=\''+ tag +'\', /hardwireDSST, \
         /interface, obsArr=obsArr, dateArr=dateArr, vdOut=vdOut')
    runOutput = idl.ev('vdOut')
#At this point, the vd files have been created
#vd files have been stored in '/tous/mir7/interface/pid_of_user'
# ************** VANK HERE  ***********************





# ############################# #
# EVERYTHING BELOW IS FOR EMAIL #
############################### #


# Message which is to be sent in email
message = ('Yale Chiron Interface Run information \n\n'
        'Proposal ID: ' + pID + '\n'
        'Star: ' + starName + '\n'
        'Created DSST: ' + str(not oldDSST) +'\n')
if (not oldDSST):
    message += ('Template Observations: '+ dsstTemplate +'\n'
            'DSST B-star Observations: '+ dsstBstars + '\n')
message += ('\nDoppler Observations: ' + dopplerArray
        '\nOutput vd Files: ' + runOutput
        '\n\n\nPlease contact Scott Smith at scott.smith@yale.edu with any \
        questions or comments')

#set up email parameters.
emailfrom = "chironinterface@gmail.com"
emailto = toaddrs
fileToSend = '' #TODO: INPUT FILE TO SEND
filename = '' #TODO: INPUT FILENAME
username = "chironinterface"
password = "dopplerInterface2016"

msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = emailto
msg["Subject"] = "Subject Line" # TODO: MAKE THIS
msg.preamble = message

ctype, encoding = mimetypes.guess_type(fileToSend)
if ctype is None or encoding is not None:
    ctype = "application/octet-stream"

maintype, subtype = ctype.split("/", 1)

if maintype == "text":
    fp = open(fileToSend)
    # Note: we should handle calculating the charset
    attachment = MIMEText(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "image":
    fp = open(fileToSend, "rb")
    attachment = MIMEImage(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "audio":
    fp = open(fileToSend, "rb")
    attachment = MIMEAudio(fp.read(), _subtype=subtype)
    fp.close()
else:
    print("this should happen")
    fp = open(fileToSend, "rb")
    attachment = MIMEBase(maintype, subtype)
    attachment.set_payload(fp.read())
    fp.close()
    encoders.encode_base64(attachment)
attachment.add_header("Content-Disposition", "attachment", filename=filename)
msg.attach(attachment)

server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(username,password)
server.sendmail(emailfrom, emailto, msg.as_string())
server.quit()
