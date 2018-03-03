#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# Title      : Data over udp/packetizer/rssi test script
#-----------------------------------------------------------------------------
# File       : udpDataTest.py
# Created    : 2018-03-02
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
import rogue.protocols.udp
import rogue.interfaces.stream
import pyrogue
import time

# Server chain
serv = rogue.protocols.udp.Server(8192,1024);
port = serv.getPort()
print("Port is {}".format(port))

sRssi = rogue.protocols.rssi.Server(1024)
#pyrogue.streamConnectBiDir(serv,sRssi.transport())

#sPack = rogue.protocols.packetizer.Core(1024)
#pyrogue.streamConnectBiDir(sRssi.application(),sPack.transport())

prbsRx = rogue.utilities.Prbs()
#pyrogue.streamConnect(sPack.application(0),prbsRx)

# Client chain
#client = rogue.protocols.udp.Client("localhost",port,1024);

cRssi = rogue.protocols.rssi.Client(1024)
#pyrogue.streamConnectBiDir(client,sRssi.transport())

#cPack = rogue.protocols.packetizer.Core(1024)
#pyrogue.streamConnectBiDir(cRssi.application(),cPack.transport())

prbsTx = rogue.utilities.Prbs()
#pyrogue.streamConnect(prbsTx,cPack.application(0))

pyrogue.streamConnectBiDir(sRssi.transport(),cRssi.transport())

# Enable 
#prbsTx.enable(1000)

while (True):

   print("")
   print(" Source: Count {}, Bytes {}".format(prbsTx.getTxCount(),prbsTx.getTxBytes()))
   print(" Dest:   Count {}, Bytes {}, Errors {}".format(prbsRx.getRxCount(),prbsRx.getRxBytes(),prbsRx.getRxErrors()))
   time.sleep(1)

