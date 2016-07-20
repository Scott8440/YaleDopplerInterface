# YaleDopplerInterface

Dop_old_interface README

This directory was created to host all of the doppler code which is modified
to be run through the CHIRON web interface. A list of all changes to the code is
included here, along with a description of how the interface uses it



CHANGELOG:

File              Date            Line #   Comments

dr_run            08/11/16        Many     Commented out the hardcoded tag name
                                            so it must use the one specified as argument
dr_run            08/11/16        31       Changed hardcoded dsst name just for
                                            testing purposes
crank.pro         08/11/16        178      Commented out a stop. Didn't know
                                            why it was there
cf_new.pro        08/14/16        47       Added back a check for iodcell. When
                                            it was removed it caused the doppler
                                            code to run on template observations
make_dsst         08/14/16        167      Block that creates vdArr from the input
                                            iodine observations
vdiodbatch        08/19/16        Many     Made it so interfaceArr keyword Can
                                            be specified and it only runs those
                                            observations. Also ouptputFiles is
                                            an array that holds the vd filenames
                                            after it is finished. tag must now
                                            be specified as well
reduce.pro        08/19/16        68       Added a block to manually create the
                                            cf arry out of the provided obs instead
                                            of looking up every one from that year
crank.pro         08/19/16        ##       Added vdOut tag to hold output of all
                                            vd files in an array


Needed Changes:

dr_run:           Change the way it finds observations to be just from the input
                  so it doesn't run an entire year each time you call it.
                  (NOTE: DONE)

make_dsst:        Change how it gets the bookends to come from the input. Use
                  lines 36-41 as a guide for how to set up the vdx array
                  (NOTE: DONE)

Overall:          Document everything
                  Check hardcoded directory locations




Other Notes

dop_rayclean: Presumed stable and robust on 08/14/16

  Calling Procedure Example (from dop1):
  IDL> obsnm = 'achi120710.'+strcompress(string(indgen(3)+1140), /REMOVE_ALL)
  IDL> dopenv = ctio4k_init('achi120710.1140', 'junk', 0.0, iss_obnm='junk', date='120710', tag='ss’)
  IDL> dop_rayclean, obsnm, dopenv=dopenv, observatory='ctio4k', obstack=obstack, star=star, mdtck=5.0, /auto


Update on Calling make_dsst:

  Use the iodine observations specified from the site to pass to make_dsst.
  These are passed through the keyword iodArr. If it's not passed through, it
  will look them up through hardwired paths.
