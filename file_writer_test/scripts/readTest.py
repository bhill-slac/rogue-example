#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# Title      : Read test data from a file
#-----------------------------------------------------------------------------
# File       : readTest.py
# Created    : 2018-03-14
#-----------------------------------------------------------------------------
# This file is part of the rogue_example software. It is subject to 
# the license terms in the LICENSE.txt file found in the top-level directory 
# of this distribution and at: 
#    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html. 
# No part of the rogue_example software, including this file, may be 
# copied, modified, propagated, or distributed except according to the terms 
# contained in the LICENSE.txt file.
#-----------------------------------------------------------------------------
import rogue.utilities 
import rogue.utilities.fileio
import rogue.interfaces.stream
import pyrogue
import time

rogue.Logging.setLevel(rogue.Logging.Debug)

frd = rogue.utilities.fileio.StreamReader()
prbsB = rogue.utilities.Prbs()
pyrogue.streamConnect(frd,prbsB)

frd.open("test.dat.1")
#frd.open("test.dat")
sec = 0
last = -1 

try:
    while (True):

       print("")
       print(" Dest: Time %i, Count %i, Bytes %i, Errors %i" % (sec, prbsB.getRxCount(),prbsB.getRxBytes(),prbsB.getRxErrors()))

       if ( last == prbsB.getRxBytes() ):
           print("")
           print("Done in {} seconds".format(sec))
           break;
       last = prbsB.getRxBytes()
        
       time.sleep(1)
       sec += 1

except KeyboardInterrupt:
    pass

