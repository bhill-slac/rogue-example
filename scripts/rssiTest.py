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
import rogue.protocols.udp
import rogue.protocols.rssi

# UDP
udp = rogue.protocols.udp.Client("192.168.2.126",8192,1500)

# RSSI
rssi = rogue.protocols.rssi.Core(1500)

# Attached RSSI transport to UDP
pyrogue.streamConnectBiDir(rssi.transport(),udp)

# Close window and stop polling
def stop():
    exit()

# Start with ipython -i scripts/evalBoard.py
print("Ready")

