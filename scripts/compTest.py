#!/usr/bin/env python3
import pyrogue
import rogue.utilities 
import rogue.interfaces.stream
import time

prbsA = rogue.utilities.Prbs()
#compA = rogue.utilities.StreamZip()
#compB = rogue.utilities.StreamUnZip()
prbsB = rogue.utilities.Prbs()

#pyrogue.streamConnect(prbsA,compA)
#pyrogue.streamConnect(compA,compB)
#pyrogue.streamConnect(compB,prbsB)
pyrogue.streamConnect(prbsA,prbsB)

prbsA.enable(1000)
#prbsA.genFrame(1000)

while (True):

   print("")
   print(" Dest: Count %i, Bytes %i, Errors %i" % (prbsB.getRxCount(),prbsB.getRxBytes(),prbsB.getRxErrors()))
   time.sleep(1)

