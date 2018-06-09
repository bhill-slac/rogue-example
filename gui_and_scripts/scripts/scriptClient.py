#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# Title      : Script Client
#-----------------------------------------------------------------------------
# File       : scriptClient.py
# Created    : 2016-09-29
#-----------------------------------------------------------------------------
# Description:
# Generic Script client for rogue
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

# Set host= to the address of a network interface to secificy the network to use
# Set ns= to the address of the nameserver(optional)
client = pyrogue.PyroClient(group='testGroup', localAddr=None, nsAddr=None)
dummyTree = client.getRoot('dummyTree')

dummyTree.AxiVersion.ScratchPad.set(0x55)
print(dummyTree.AxiVersion.ScratchPad.get(0x55))

# Start with ipython -i scriptClient.py to interact with the tree
