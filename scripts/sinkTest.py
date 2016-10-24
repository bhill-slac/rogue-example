#!/usr/bin/env python
#-----------------------------------------------------------------------------
# Title      : File read and write test
#-----------------------------------------------------------------------------
# File       : exoTest.py
# Author     : Ryan Herbst, rherbst@slac.stanford.edu
# Created    : 2016-09-29
# Last update: 2016-09-29
#-----------------------------------------------------------------------------
# Description:
# File read and write test
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
import rogue_example
import pyrogue
import time

prbsA = rogue.utilities.Prbs()
sink = rogue_example.StreamSink()
pyrogue.streamConnect(prbsA,sink)

print("Generating data for 5 seconds")
prbsA.enable(1000)
time.sleep(5)
prbsA.disable()
time.sleep(1)

print("Generated: Count %i, Bytes %i" % (prbsA.getTxCount(),prbsA.getTxBytes()))
print("      Got: Count %i, Bytes %i" % (sink.getRxCount(),sink.getRxBytes()))

