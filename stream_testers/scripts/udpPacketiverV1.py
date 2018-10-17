#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# Title      : Data over udp/packetizer/rssi test script
#-----------------------------------------------------------------------------
# File       : udpPacketizerV1.py
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

#rogue.Logging.setLevel(rogue.Logging.Info)
rogue.Logging.setLevel(rogue.Logging.Warning)
#rogue.Logging.setLevel(rogue.Logging.Debug)

# Server chain
serv = rogue.protocols.udp.Server(0,False);
port = serv.getPort()
print("Port is {}".format(port))

sRssi = rogue.protocols.rssi.Server(serv.maxPayload())
pyrogue.streamConnectBiDir(serv,sRssi.transport())

sPack = rogue.protocols.packetizer.Core()
pyrogue.streamConnectBiDir(sRssi.application(),sPack.transport())

prbsRx = rogue.utilities.Prbs()
pyrogue.streamConnect(sPack.application(0),prbsRx)

# Client chain
client = rogue.protocols.udp.Client("localhost",port,False);

cRssi = rogue.protocols.rssi.Client(client.maxPayload())
pyrogue.streamConnectBiDir(client,cRssi.transport())

cPack = rogue.protocols.packetizer.Core()
pyrogue.streamConnectBiDir(cRssi.application(),cPack.transport())

prbsTx = rogue.utilities.Prbs()
pyrogue.streamConnect(prbsTx,cPack.application(0))

sRssi.start()
cRssi.start()

# Enable 
prbsTx.enable(20000)

try:
    while (True):
       print("")
       print(" Source: Open {}, Count {}, Bytes {} Drops {} Retrans {}".format(cRssi.getOpen(),prbsTx.getTxCount(),prbsTx.getTxBytes(),cRssi.getDropCount(),cRssi.getRetranCount()))
       print(" Dest:   Open {}, Count {}, Bytes {} Drops {} Retrans {} Errors {}".format(sRssi.getOpen(),prbsRx.getRxCount(),prbsRx.getRxBytes(),sRssi.getDropCount(),sRssi.getRetranCount(), prbsRx.getRxErrors()))
       time.sleep(1)

except KeyboardInterrupt:
    pass

