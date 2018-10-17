#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# Title      : Direct RSSI to RSSI connection tester
#-----------------------------------------------------------------------------
# File       : rssiTest.py
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

#rogue.Logging.setLevel(rogue.Logging.Debug)

rogue.Logging.setFilter("pyrogue.rssi.controller",rogue.Logging.Debug)

sRssi = rogue.protocols.rssi.Server(1400)

sPack = rogue.protocols.packetizer.CoreV2(False,True,True)
pyrogue.streamConnectBiDir(sRssi.application(),sPack.transport())

prbsRx = rogue.utilities.Prbs()
pyrogue.streamConnect(sPack.application(0),prbsRx)

cRssi = rogue.protocols.rssi.Client(1400)

cPack = rogue.protocols.packetizer.CoreV2(True,True),True
pyrogue.streamConnectBiDir(cRssi.application(),cPack.transport())

prbsTx = rogue.utilities.Prbs()
pyrogue.streamConnect(prbsTx,cPack.application(0))

# This does not work! Need a buffer copy here!
pyrogue.streamConnectBiDir(cRssi.transport(),sRssi.transport())

sRssi.start()
cRssi.start()

# Enable 
prbsTx.enable(20000)

try:
    while (True):
       print("")
       print(" Source: Open {}, Count {}, Bytes {}".format(cRssi.getOpen(),prbsTx.getTxCount(),prbsTx.getTxBytes()))
       print(" Dest:   Open {}, Count {}, Bytes {}, Errors {}".format(sRssi.getOpen(),prbsRx.getRxCount(),prbsRx.getRxBytes(),prbsRx.getRxErrors()))
       time.sleep(1)

except KeyboardInterrupt:
    pass

