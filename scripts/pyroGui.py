#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# Title      : GUI Client
#-----------------------------------------------------------------------------
# File       : guiClient.py
# Author     : Ryan Herbst, rherbst@slac.stanford.edu
# Created    : 2016-09-29
# Last update: 2016-09-29
#-----------------------------------------------------------------------------
# Description:
# Generic GUI client for rogue
#-----------------------------------------------------------------------------
# This file is part of the rogue_example software. It is subject to 
# the license terms in the LICENSE.txt file found in the top-level directory 
# of this distribution and at: 
#    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html. 
# No part of the rogue_example software, including this file, may be 
# copied, modified, propagated, or distributed except according to the terms 
# contained in the LICENSE.txt file.
#-----------------------------------------------------------------------------
import Pyro4
import PyQt4.QtGui
import sys
import pyrogue.gui

import pyroLib
import threading
import surf.axi
import collections

cb = pyroLib.CbClass()

#with Pyro4.core.Daemon() as daemon:
#    cb = pyroLib.CbClass()
#    daemon.register(cb)
#
#    evalBoard = Pyro4.Proxy("PYRONAME:evalBoard")
#    evalBoard.addVarListener(cb.rootCb)
#
#    daemon.requestLoop()

def recreate_OrderedDict(name, values):
    return collections.OrderedDict(values['items'])

Pyro4.util.SerializerBase.register_dict_to_class("collections.OrderedDict", recreate_OrderedDict)

Pyro4.util.SerializerBase.register_dict_to_class("collections.OrderedDict", recreate_OrderedDict)
daemon = Pyro4.Daemon()

def server():
    daemon.requestLoop()

t1 = threading.Thread(target=server)
t1.start()

evalBoard = pyrogue.PyroRoot(Pyro4.Proxy("PYRONAME:evalBoard"),daemon)
#enable    = Pyro4.Proxy("PYRONAME:enable")
#UpTimeCnt = Pyro4.Proxy("PYRONAME:UpTimeCnt")

#UpTimeCnt.addListener(tst)
#evalBoard.addVarListener(tstA)

# Create GUI
appTop = PyQt4.QtGui.QApplication(sys.argv)
guiTop = pyrogue.gui.GuiTop('rogueTest')
guiTop.addTree(evalBoard)

# Run gui
appTop.exec_()

