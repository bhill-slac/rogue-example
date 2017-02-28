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
import pyrogue.epics
import pyrogue.utilities.prbs
import logging

#logging.getLogger('pyrogue.Block').setLevel(logging.DEBUG)

udpRssiA = pyrogue.protocols.UdpRssiPack("192.168.2.187",8193,1500)
rssiSrp = rogue.protocols.srp.SrpV3()
pyrogue.streamConnectBiDir(rssiSrp,udpRssiA.application(0))

#udpRssiB = pyrogue.protocols.UdpRssiPack("192.168.2.187",8194,1500)
#prbsRx = pyrogue.utilities.prbs.PrbsRx('prbsRx')
#pyrogue.streamConnect(udpRssiB.application(1),prbsRx)

#testRx = DataRx()
#pyrogue.streamConnect(udpRssiB.application(1),testRx)

#sink = rogue_example.StreamSink()
#pyrogue.streamConnect(udpRssiB.application(1),sink)

evalBoard = pyrogue.Root('rssiBoard','Evaluation Board')
#evalBoard.add(prbsRx)

evalBoard.add(surf.AxiVersion.create(memBase=rssiSrp,offset=0x00000000))
evalBoard.add(surf.SsiPrbsTx.create(memBase=rssiSrp,offset=0x0A030000))
evalBoard.add(surf.Rssi(memBase=rssiSrp,offset=0x0A050000))

# Create mesh node
mNode = pyrogue.mesh.MeshNode('rssiTest',iface='eth3',root=evalBoard)
mNode.start()

epics = pyrogue.epics.EpicsCaServer('rssiTest',evalBoard)
epics.start()

# Close window and stop polling
def stop():
    mNode.stop()
    epics.stop()
    evalBoard.stop()
    exit()

# Start with ipython -i scripts/evalBoard.py
print("Started")

#st = 0
#lc = 0
#base = 0
while(True):
    time.sleep(1)
#    print("Link State: RSSIOpen=%i, RSSIBusy=%i, DownCount=%i, RssiDropCount=%i, RssiReTrans=%i, PackDropCount=%i" 
#          % (udpRssiB.getRssiOpen(),udpRssiB.getRssiBusy(),udpRssiB.getRssiDownCount(),udpRssiB.getRssiDropCount(),
#           udpRssiB.getRssiRetranCount(),udpRssiB.getPackDropCount()))

#    count = sink.getRxCount()
#    total = sink.getRxBytes()

#    if (count - lc) > 100:
#        w = ((total-base)*8.0) / ((time.time() - st) * 1.0e9)
#        print("Rx Count = %i, Rx Bytes = %i, BW = %f" % (count,total,w))
#        st = time.time()
#        base = total
#        lc = count

