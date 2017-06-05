#!/usr/bin/env python
#-----------------------------------------------------------------------------
# Title      : Script Client
#-----------------------------------------------------------------------------
# File       : guiClient.py
# Author     : Ryan Herbst, rherbst@slac.stanford.edu
# Created    : 2016-09-29
# Last update: 2016-09-29
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
import pyrogue.gui
import sys

group = 'rogueTest'
iface = '127.0.0.1'

client = pyrogue.PyroClient('rogueTest')
evalBoard = client.getRoot('evalBoard')

def stop():
    client.stop()
    exit()

