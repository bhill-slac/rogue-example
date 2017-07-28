#!/usr/bin/env python3
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
import pyrogue 

#client = pyrogue.PyroClient(group='rogueTest',host='134.79.229.11',ns='134.79.229.11')
#client = pyrogue.PyroClient(group='rogueTest',host='134.79.229.11')
client = pyrogue.PyroClient(group='rogueTest')
evalBoard = client.getRoot('evalBoard')

