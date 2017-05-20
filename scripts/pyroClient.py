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

blah = Pyro4.Proxy("PYRONAME:blah")

print("Type   = {}".format(type(blah)))
#print("Test   = {}".format(evalBoard.test))
#print("Name   = {}".format(evalBoard.name))
#node = evalBoard.getNode()
#node = evalBoard.root
#print("Type={}".format(type(node)))

#appTop = PyQt4.QtGui.QApplication(sys.argv)
#guiTop = pyrogue.gui.GuiTop('rogueTest')
#guiTop.addTree(evalBoard)

# Run gui
#appTop.exec_()


