#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# Title      : RSSI Testing
#-----------------------------------------------------------------------------
# File       : rssiTest.py
# Author     : Ryan Herbst, rherbst@slac.stanford.edu
# Created    : 2017-01-11
# Last update: 2017-01-11
#-----------------------------------------------------------------------------
# Description:
# Rogue interface to rssi servers
#-----------------------------------------------------------------------------
# This file is part of the rogue_example software. It is subject to 
# the license terms in the LICENSE.txt file found in the top-level directory 
# of this distribution and at: 
#    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html. 
# No part of the rogue_example software, including this file, may be 
# copied, modified, propagated, or distributed except according to the terms 
# contained in the LICENSE.txt file.
#-----------------------------------------------------------------------------
import atexit
import time
import sys
import pyrogue
import pyrogue.protocols
import rogue.protocols.srp
import rogue.protocols.udp
import surf
import surf.AxiVersion
import surf.SsiPrbsTx
import pyrogue.mesh
import pyrogue.utilities.prbs


class DataRx(rogue.interfaces.stream.Slave):

   def __init__(self):
      rogue.interfaces.stream.Slave.__init__(self)
      self.b = 0
      self.c = 0

   def _acceptFrame(self,frame):
      self.c += 1
      self.b += frame.getPayload()

   def getCount(self):
      return self.c,self.b


udpRssiA = pyrogue.protocols.UdpRssiPack("192.168.2.187",8193,1500)
rssiSrp = rogue.protocols.srp.SrpV3()
pyrogue.streamConnectBiDir(rssiSrp,udpRssiA.application(0))

udpRssiB = pyrogue.protocols.UdpRssiPack("192.168.2.187",8194,1500)
#prbsRx = pyrogue.utilities.prbs.PrbsRx('prbsRx')
#pyrogue.streamConnect(udpRssiB.application(1),prbsRx)

testRx = DataRx()
pyrogue.streamConnect(udpRssiB.application(1),testRx)

evalBoard = pyrogue.Root('evalBoard','Evaluation Board')
#evalBoard.add(prbsRx)

evalBoard.add(surf.AxiVersion.create(memBase=rssiSrp,offset=0x00000000))
evalBoard.add(surf.SsiPrbsTx.create(memBase=rssiSrp,offset=0x0A030000))
evalBoard.add(surf.Rssi(memBase=rssiSrp,offset=0x0A050000))

# Create mesh node
mNode = pyrogue.mesh.MeshNode('rogueTest',iface='eth3',root=evalBoard)
mNode.start()

# Close window and stop polling
def stop():
    mNode.stop()
    evalBoard.stop()
    exit()

# Start with ipython -i scripts/evalBoard.py
print("Started")

l = 0
while(True):
    time.sleep(1)
    print("Link State: RSSIOpen=%i, RSSIBusy=%i, DownCount=%i, RssiDropCount=%i, RssiReTrans=%i, PackDropCount=%i" 
          % (udpRssiB.getRssiOpen(),udpRssiB.getRssiBusy(),udpRssiB.getRssiDownCount(),udpRssiB.getRssiDropCount(),
           udpRssiB.getRssiRetranCount(),udpRssiB.getPackDropCount()))
    c,b = testRx.getCount()
    w = ((b-l)*8.0) / 1e9
    l = b
    print("Rx Count = %i, Rx Bytes = %i, BW = %f" % (c,b,w))


