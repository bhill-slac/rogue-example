#!/usr/bin/env python
#-----------------------------------------------------------------------------
# Title      : RCE testl instance
#-----------------------------------------------------------------------------
# File       : rceTest.py
# Author     : Ryan Herbst, rherbst@slac.stanford.edu
# Created    : 2016-10-24
# Last update: 2016-10-24
#-----------------------------------------------------------------------------
# Description:
# Rogue interface to RCE test
#-----------------------------------------------------------------------------
# This file is part of the rogue_example software. It is subject to 
# the license terms in the LICENSE.txt file found in the top-level directory 
# of this distribution and at: 
#    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html. 
# No part of the rogue_example software, including this file, may be 
# copied, modified, propagated, or distributed except according to the terms 
# contained in the LICENSE.txt file.
#-----------------------------------------------------------------------------
import rce.RceCommon
import rogue.hardware.rce
import pyrogue
import pyrogue.mesh
import pyrogue.epics

# Set base
rceTest = pyrogue.Root('rceTest','RCE')

# RCE Maped Memory
rceMap = rogue.hardware.rce.MapMemory()
rceMap.addMap(0x80000000,0x2000)
rceMap.addMap(0x84000000,0x1000)

# Add Devices
rceTest.add(rce.RceCommon.create(memBase=rceMap))

# Create mesh node
mNode = pyrogue.mesh.MeshNode('rogueTest',root=rceTest)
mNode.start()

# Create epics node
epics = pyrogue.epics.EpicsCaServer('rogueTest',rceTest)
epics.start()

# Close window and stop polling
def stop():
    mNode.stop()
    epics.stop()
    rceTest.stop()
    exit()

# Start with ipython -i scripts/evalBoard.py
print("Started rogue mesh and epics V3 server. To exit type stop()")

