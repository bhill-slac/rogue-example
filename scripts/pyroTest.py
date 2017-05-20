#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# Title      : Eval board instance
#-----------------------------------------------------------------------------
# File       : evalBoard.py
# Author     : Ryan Herbst, rherbst@slac.stanford.edu
# Created    : 2016-09-29
# Last update: 2016-09-29
#-----------------------------------------------------------------------------
# Description:
# Rogue interface to eval board
#-----------------------------------------------------------------------------
# This file is part of the rogue_example software. It is subject to 
# the license terms in the LICENSE.txt file found in the top-level directory 
# of this distribution and at: 
#    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html. 
# No part of the rogue_example software, including this file, may be 
# copied, modified, propagated, or distributed except according to the terms 
# contained in the LICENSE.txt file.
#-----------------------------------------------------------------------------
import pyrogue.utilities.prbs
import pyrogue.utilities.fileio
import rogue.interfaces.stream
import pyrogue.mesh
import pyrogue.epics
import surf.axi
import surf.protocols.ssi
import threading
import signal
import atexit
import yaml
import time
import sys
import testBridge
import logging
import Pyro4

#Pyro4.config.REQUIRE_EXPOSE = False

import pyroLib

blah = pyroLib.TestB()

#daemon = Pyro4.Daemon()
#ns = Pyro4.locateNS()
#uri = daemon.register(evalBoard)
#ns.register('rogueTest',uri)
#daemon.requestLoop()
Pyro4.Daemon.serveSimple ( 
    {
        pyroLib.TestA: None,
        pyroLib.TestB: None,
        blah:  'blah'
    }, ns = True
)

