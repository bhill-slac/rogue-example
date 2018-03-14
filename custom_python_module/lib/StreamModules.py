#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# Title      : Stream module examples
#-----------------------------------------------------------------------------
# File       : StreamModules.py
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
import pyrogue
import rogue.interfaces.stream
import time

# Stream receiver
class StreamRx(rogue.interfaces.stream.Slave):

    def __init__(self):
        rogue.interfaces.stream.Slave.__init__(self)

    def _acceptFrame(self,frame):
        p = bytearray(frame.getPayload())
        frame.read(p,0)
        print("-----------------------------------------------------")
        print("Got frame with size {}".format(frame.getPayload()))
        print("First four bytes {:02x} {:02x} {:02x} {:02x}".format(p[0],p[1],p[2],p[3]))
 
# Stream transmitter
class StreamTx(rogue.interfaces.stream.Master):

    def __init__(self):
       rogue.interfaces.stream.Master.__init__(self)

    def generate(self):
        # size=100, zeroCopyEn=True
        frame = self._reqFrame(100,True)
        p = bytearray(100)
        for i in range(100):
            p[i] = 0xA
        frame.write(p,0)
        self._sendFrame(frame)

# Stream processors
class StreamProc(rogue.interfaces.stream.Master,rogue.interfaces.stream.Slave):

    def __init__(self):
       rogue.interfaces.stream.Master.__init__(self)
       rogue.interfaces.stream.Slave.__init__(self)

    def _acceptFrame(self,frame):
        p = bytearray(frame.getPayload())
        frame.read(p,0)

        # size=payload, zeroCopyEn=True
        frameOut = self._reqFrame(frame.getPayload(),True)

        for i in range(frame.getPayload()):
            p[i] += 3

        frameOut.write(p,0)
        self._sendFrame(frameOut)

