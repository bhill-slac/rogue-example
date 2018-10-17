#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# Title      : Packetizer to packetizer test
#-----------------------------------------------------------------------------
# File       : packetizerTestV2.py
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

sPack = rogue.protocols.packetizer.CoreV2(True,True,True)
prbsRx = rogue.utilities.Prbs()
pyrogue.streamConnect(sPack.application(0),prbsRx)

cPack = rogue.protocols.packetizer.CoreV2(True,True,True)
prbsTx = rogue.utilities.Prbs()
pyrogue.streamConnect(prbsTx,cPack.application(0))

pyrogue.streamConnectBiDir(cPack.transport(),sPack.transport())

# Enable 
prbsTx.enable(20004)

try:
    while (True):
       print("")
       print(" Source: Count {}, Bytes {}".format(prbsTx.getTxCount(),prbsTx.getTxBytes()))
       print(" Dest:   Count {}, Bytes {}, Errors {}".format(prbsRx.getRxCount(),prbsRx.getRxBytes(),prbsRx.getRxErrors()))
       time.sleep(1)

except KeyboardInterrupt:
    pass

