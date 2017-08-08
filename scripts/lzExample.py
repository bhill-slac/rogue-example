#!/usr/bin/env python3
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
        # size=100, zeroCopyEn=True, maxBuffSize=0
        frame = self._reqFrame(100,True,0)
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

        # size=payload, zeroCopyEn=True, maxBuffSize=0
        frameOut = self._reqFrame(frame.getPayload(),True,0)

        for i in range(frame.getPayload()):
            p[i] += 3

        frameOut.write(p,0)
        self._sendFrame(frameOut)

gen = StreamTx()
prc = StreamProc()
rx  = StreamRx()

pyrogue.streamConnect(gen,prc)
pyrogue.streamConnect(prc,rx)

while(True):
    time.sleep(1)
    gen.generate()

