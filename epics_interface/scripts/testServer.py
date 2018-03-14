#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# Title      : EPICS test script
#-----------------------------------------------------------------------------
# File       : testServer.py
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
import pyrogue.protocols.epics
import rogue.interfaces.stream
import surf.axi
import time
import rogue

#rogue.Logging.setLevel(rogue.Logging.Debug)

class EpicsStream(rogue.interfaces.stream.Slave,rogue.interfaces.stream.Master):
    def __init__(self):
        rogue.interfaces.stream.Slave.__init__(self)
        rogue.interfaces.stream.Master.__init__(self)

    def _acceptFrame(self,frame):
        print("Got frame: size={}".format(frame.getPayload()))

    def genFrame(self,size):
        frame = self._reqFrame(size,True)
        ba = bytearray(size)
        frame.write(ba,0)
        self._sendFrame(frame)

def printVal(path,value,disp):
    print(f"Var set {path}, value {value}, disp {disp}")

class DummyTree(pyrogue.Root):

    def __init__(self):

        pyrogue.Root.__init__(self,name='dummyTree',description="Dummy tree for example")

        # Use a memory space emulator
        sim = pyrogue.interfaces.simulation.MemEmulate()
        
        # Add Device
        self.add(surf.axi.AxiVersion(memBase=sim,offset=0x0))
        self.AxiVersion.ScratchPad.addListener(printVal)

        self.epicsStream = EpicsStream()

        v = (pyrogue.LocalVariable(name='listVar',value=[0,1,2,3,4,5,6,7,8,9,10]))
        v.addListener(printVal)
        self.add(v)

        v = (pyrogue.LocalVariable(name='strVar',value="test"))
        v.addListener(printVal)
        self.add(v)

        # Start the tree
        self.start()

        self.epics = pyrogue.protocols.epics.EpicsCaServer(base='test',root=self)
        es = self.epics.createSlave('slave',1000,'UInt32')
        em = self.epics.createMaster('mast',1000,'UInt32')
        self.epics.start()

        pyrogue.streamConnect(em, self.epicsStream)
        pyrogue.streamConnect(self.epicsStream, es)

if __name__ == "__main__":

    dummyTree = DummyTree()

    print("Running in python main")
    try:
        while True:
            for i in range(4,16,4):
                print("Sending {}".format(i))
                dummyTree.epicsStream.genFrame(i)
                lst = [i for i in range(i)]
                print("Setting: {}".format(lst))
                dummyTree.listVar.set(lst)
                time.sleep(1)
    except KeyboardInterrupt:
        dummyTree.stop()

