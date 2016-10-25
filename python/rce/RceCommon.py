#!/usr/bin/env python
#-----------------------------------------------------------------------------
# Title      : PyRogue RCE Common Module
#-----------------------------------------------------------------------------
# File       : RceCommon.py
# Author     : Ryan Herbst, rherbst@slac.stanford.edu
# Created    : 2016-10-24
# Last update: 2016-10-24
#-----------------------------------------------------------------------------
# Description:
# PyRogue RCE Common Module
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
import collections

def create(name='rceCommon', offset=0x80000000, memBase=None, hidden=False):
    """Create the RCE Common Device"""

    dev = pyrogue.Device(name=name, memBase=memBase, offset=offset, hidden=hidden, size=0x5000000,
                         description='RCE Common Registers')

    dev.add(pyrogue.Variable(name='fpgaVersion', description='FPGA Firmware Version Number',
                             offset=0x00, bitSize=32, bitOffset=0, base='hex', mode='RO'))

    dev.add(pyrogue.Variable(name='rceVersion', description='RCE Software Version',
                             offset=0x08, bitSize=32, bitOffset=0, base='hex', mode='RO'))

    dev.add(pyrogue.Variable(name='deviceDna', description='Xilinx Device DNA value burned into FPGA',
                             offset=0x20, bitSize=64, bitOffset=0, base='hex', mode='RO'))

    dev.add(pyrogue.Variable(name='eFuseValue', description='Xilinx E-Fuse Value',
                             offset=0x30, bitSize=32, bitOffset=0, base='hex', mode='RO'))

    dev.add(pyrogue.Variable(name='ethMode', description='Ethernet Mode',
                             offset=0x34, bitSize=32, bitOffset=0, base='hex', mode='RO'))

    dev.add(pyrogue.Variable(name='heartBeat', description='Incrementing Counter', pollEn=True,
                             offset=0x38, bitSize=32, bitOffset=0, base='uint', mode='RO'))

    dev.add(pyrogue.Variable(name='buildStamp', description='Firmware build string',
                             offset=0x1000, bitSize=256*8, bitOffset=0, base='string', mode='RO'))

    dev.add(pyrogue.Variable(name='serialNumber', description='RCE Board Serial Number',
                             offset=0x4000140, bitSize=64, bitOffset=0, base='hex', mode='RO'))

    dev.add(pyrogue.Variable(name='cobElement', description='COB Element Number',
                             offset=0x4000148, bitSize=8, bitOffset=0, base='hex', mode='RO'))

    dev.add(pyrogue.Variable(name='cobBay', description='COB Bay Number',
                             offset=0x4000148, bitSize=8, bitOffset=8, base='hex', mode='RO'))

    dev.add(pyrogue.Variable(name='atcaSlot', description='ATCA Slot Number',
                             offset=0x4000148, bitSize=8, bitOffset=16, base='hex', mode='RO'))

    return dev
