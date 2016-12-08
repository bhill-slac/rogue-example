#!/usr/bin/env python
#-----------------------------------------------------------------------------
# Title      : Simulation test
#-----------------------------------------------------------------------------
# File       : simTest.py
# Author     : Ryan Herbst, rherbst@slac.stanford.edu
# Created    : 2016-09-29
# Last update: 2016-09-29
#-----------------------------------------------------------------------------
# Description:
# Simulation test
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
import pyrogue
import pyrogue.simulation
import time

prbsA = rogue.utilities.Prbs()
prbsB = rogue.utilities.Prbs()

sim = pyrogue.simulation.StreamSim('localhost',20,True)

pyrogue.streamConnect(prbsA,sim)
pyrogue.streamConnect(sim,prbsB)

prbsA.enable(1000)
prbsB.enMessages(True)

while (True):

   print("Generated: Count %i, Bytes %i" % (prbsA.getTxCount(),prbsA.getTxBytes()))
   print(" Received: Count %i, Bytes %i, Errors %i" % (prbsB.getRxCount(),prbsB.getRxBytes(),prbsB.getRxErrors()))
   print("  Gateway: TxCount %i, RxCount %i" % (sim.txCount,sim.rxCount))
   #prbsA.genFrame(100)
   sim.sendOpCode(0xaa)
   sim.setData(0x7f)
   time.sleep(1)


