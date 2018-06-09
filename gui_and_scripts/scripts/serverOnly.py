#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# Title      : Server only test script
#-----------------------------------------------------------------------------
# File       : serverOnly.py
# Created    : 2018-02-28
#-----------------------------------------------------------------------------
# This file is part of the rogue_example software. It is subject to 
# the license terms in the LICENSE.txt file found in the top-level directory 
# of this distribution and at: 
#    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html. 
# No part of the rogue_example software, including this file, may be 
# copied, modified, propagated, or distributed except according to the terms 
# contained in the LICENSE.txt file.
#-----------------------------------------------------------------------------
import pyrogue
import pyrogue.interfaces.simulation
import rogue.interfaces.stream
import surf.axi
import time
import rogue

#rogue.Logging.setLevel(rogue.Logging.Debug)
import logging
logger = logging.getLogger('pyrogue')
logger.setLevel(logging.INFO)

class DummyTree(pyrogue.Root):

    def __init__(self):

        pyrogue.Root.__init__(self,name='dummyTree',description="Dummy tree for example")

        # Use a memory space emulator
        sim = pyrogue.interfaces.simulation.MemEmulate()
        
        # Add Device
        self.add(surf.axi.AxiVersion(memBase=sim,offset=0x0))

        # Start the tree with pyrogue server, internal nameserver, default interface
        # Set pyroHost to the address of a network interface to specify which nework to run on
        # set pyroNs to the address of a standalone nameserver (startPyrorNs.py)
        self.start(timeout=2.0, pyroGroup='testGroup', pyroAddr=None, pyroNsAddr=None)

if __name__ == "__main__":

    dummyTree = DummyTree()

    print("Running in python main")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        dummyTree.stop()

