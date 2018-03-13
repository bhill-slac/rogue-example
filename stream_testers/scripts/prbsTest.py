#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# Title      : PRBS Testing
#-----------------------------------------------------------------------------
# File       : prbsTest.py
# Created    : 2018-03-18
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


prbsA = rogue.utilities.Prbs()
prbsB = rogue.utilities.Prbs()

pyrogue.streamConnect(prbsA,prbsB)

prbsA.enable(1000)

while (True):

   print("")
   print(" Source: Count %i, Bytes %i" % (prbsA.getTxCount(),prbsA.getTxBytes()))
   print(" Dest:   Count %i, Bytes %i, Errors %i" % (prbsB.getRxCount(),prbsB.getRxBytes(),prbsB.getRxErrors()))
   time.sleep(1)

