#skeleton.py

# This program shows how to take all the information given from the website and
# run the whole process.

import os
import pidly
import sys
import smtplib                      # For email


# Collect input of metadata from webpage. Must know exactly how data is sent in
# and especially what order it is sent in. Input must be ended with a newline

# Examples:
# If you send info simply as a string
# exString = str(input("dummy prompt: "))

# if you want to turn a string into an array, split at each space
# exStrArray = str(input("dummy prompt: ")).split(" ")

#input 1
toaddrs  = str(input())
#input 2
pID      = str(input())
#input 3
starName = str(input())              # from first drop-down
#input 4
file1str= str(input())              # obsnm for making dsst
#input 5
file2str = str(input())              # B-star for the dsst
#input 6
dop1str  = str(input())              # obs for running the program
#input 7
dop2str  = str(input())              # iodine or b-star for program

templateArr  = file1str.split(' ')        # array of the DSST template observations
tempDate = str(templateArr[0][0:6])       # extract the date for template obs
tag      = idToTag(pID)

fileDirectory = '/tous/mir7/files/'

# Use this to get an array of non-repeating dates that make up the program obs
# This is used in reduce.pro through dr_run.pro
def makeDateArray(progObs):
    dateArray = []
    for obs in progObs:
        date = obs[0:6]
        dateArray.append(date)
    dateArray = sorted(list(set(dateArray)))
    return dateArray

def findBccor(tempArr):
    midObs = tempArr[len(tempArr)/2]

    idl = pidly.IDL()
    idl('restore, \'/tous/mir7/bary/qbcvel.dat\'')
    idl('x = where(strmid(bcat.obsnm, 10, 11, /reverse_offset) eq '+ midObs + ')')
    idl('bccor = bcat[x].bc')
    bccor = idl.ev('bccor')
    idl.close()
    return bccor

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

os.chdir("/home/scottsmith/Desktop/CHIRON/fischer-dop1/dop1")
idl = pidly.IDL()
#TODO: Add check if dsst has already been created
#clean the template observations
idl.obsnm = file1str
idl('dopenv = ctio4k_init(' +templateArr[0] + ', \'junk\', 0.0, iss_obnm=\'junk\', date=\'' +obsDate + '\', tag='+tag')')
idl('dop_rayclean, obsnm, dopenv=dopenv, observatory=\'ctio4k\', obstack=obstack, star=star, mdtck=5.0, /auto')
idl('save, star, f=\'/tous/mir7/files/hd'+ starName + tag +'_achi' + tempDate + '.dat')

# make the iodine observations for the dsst
idl('cd, "/home/scottsmith/Desktop/CHIRON/dop_old_interface"')
idl.interfaceArr = interfaceArr         # TODO: Check if this works
idl('vdiodbatch, date=\'' + date + '\', mode=\'narrow_slit\', interfaceArr=interfaceArr, outputFiles=outputFiles')
outputFiles = idl.ev('outputFiles')
#TODO: Check to make sure there are a good number of output files

# Make the dsst
outfile = fileDirectory + 'dsst' + starName + tag + 'chi' + date + '.dat'
bccor = findBccor(templateArr)
idl('cd, "/home/scottsmith/Desktop/CHIRON/fischer-dop1/dop1/z_iss_jj"')
idl('specin=star')
idl('make_dsst, \'' + starName + '\', \'' + tag + '\', \'chi' + tempDate + '\', \
    specin=specin, ngrid=30, /mov, /ctio4k, interfaceArr=interfaceArr, \
    bccor=' + bccor + ', outfile=\'' + outfile + '\'')

# Now outfile contains a newly created DSST for this star

# If new DSST was created:
idl('cd, "/home/scottsmith/Desktop/CHIRON/dop_old"')
#idl('dr_run, star=\'' + starName + '\', year=\'' + year + '\', tag=\'' + tag + '\'')
idl('dr_run, star=\'' +starName+ '\', year=\'' +year+ '\', tag=\'' +tag+ '\', ')
#######################
# Running the doppler program:
#
# Check if the DSST exists
# if not, make the dsst using dsst.pro
# Then check if the vd's have been run
# Then check which of the chosen observations have been run, and run any that have
#   not yet been run
#   This is by using dr_run.pro
# Then use vank.pro to recover the velocities
# The velocites are in vst[star].dat


#set up email parameters. Others might be needed
fromaddr = 'scott8440@gmail.com'
toaddrs  = str(input("toaddrs: "))
username = 'username'
password = 'pwstring'                   # have to hardcode pw and username

#Log in to email server and send mail. Should be the last process in program
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
