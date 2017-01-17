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
import pyrogue.mesh

link = pyrogue.protocols.UdpRssiPack("192.168.2.126",8192,1500)
#link = rogue.protocols.udp.Client("192.168.2.126",8193,1500)

evalBoard = pyrogue.Root('evalBoard','Evaluation Board')

srp = rogue.protocols.srp.SrpV0()
pyrogue.streamConnectBiDir(srp,link.application(0))
#pyrogue.streamConnectBiDir(srp,link)

evalBoard.add(surf.AxiVersion.create(memBase=srp,offset=0x0))

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

while(True):
    time.sleep(1)
    print("Link State: RSSIOpen=%i, DownCount=%i, RssiDropCount=%i, RssiReTrans=%i, PackDropCount=%i" 
          %
          (link.getRssiOpen(),link.getRssiDownCount(),link.getRssiDropCount(),
           link.getRssiRetranCount(),link.getPackDropCount()))

