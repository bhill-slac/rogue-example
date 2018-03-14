#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# Title      : Example memory bridge in python
#-----------------------------------------------------------------------------
# File       : ExampleBridge.py
# Created    : 2018-03-13
#-----------------------------------------------------------------------------
# This file is part of the rogue software platform. It is subject to
# the license terms in the LICENSE.txt file found in the top-level directory
# of this distribution and at:
#    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
# No part of the rogue software platform, including this file, may be
# copied, modified, propagated, or distributed except according to the terms
# contained in the LICENSE.txt file.
#-----------------------------------------------------------------------------

import rogue.interfaces.memory
import time

class Bridge(rogue.interfaces.memory.Master,rogue.interfaces.memory.Slave):

    def __init__(self):
        rogue.interfaces.memory.Master.__init__(self)
        rogue.interfaces.memory.Slave.__init__(self,4,4)
        self.done = False
        self.err  = 0

    def _doMaxAccess(self):
        """ Respond to max access request by forwarding to downstream slave"""
        return(self._reqMaxAccess())

    def _doMinAccess(self):
        """ Respond to min access request by forwarding to downstream slave"""
        return(self._reqMinAccess())

    def _doTransaction(self,transaction):
        """ Incoming transaction request"""
        type    = transaction.type() 
        address = transaction.address() 
        size    = transaction.size() 

        # Create an byte array for outbound transaction
        ba = bytearray(size)

        # Write request, First get data from incoming transaction
        if type == rogue.interfaces.memory.Write or type == rogue.interfaces.memory.Post:
            isRead = True
            transaction.getData(ba,0)
        else:
            isRead = False
        
        # Store transaction for later, part of slave subclass
        # inId will be used for later lookup
        inId = transaction.id()
        self._addTransaction(transaction)

        # Request transaction to downstream slave, pass byte array for data, optional size and offset
        # if transaction should only access a potion of the passed data
        offset = 0
        outId = self._reqTransaction(address,ba,size,offset,type)

        # Wait for transaction to be done, Either pass the ID to wait for or
        # 0 to wait for all pending outbound transactions
        self._waitTransaction(outId)

        # Remote transaction has completed, retreive from local store
        savedTran = self._getTransaction(inId)

        # Transaction has expired
        if savedTran is None:
            return

        # If this was a read return the data
        if isRead:
            savedTran.setData(ba,0)

        # Transaction has completed without error, error = 0
        savedTran.done(0)

