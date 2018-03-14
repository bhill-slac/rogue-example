#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# Title      : Start a standalone pyro nameserver
#-----------------------------------------------------------------------------
# File       : startPyro4Ns.py
# Created    : 2016-09-29
#-----------------------------------------------------------------------------
# This file is part of the rogue_example software. It is subject to 
# the license terms in the LICENSE.txt file found in the top-level directory 
# of this distribution and at: 
#    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html. 
# No part of the rogue_example software, including this file, may be 
# copied, modified, propagated, or distributed except according to the terms 
# contained in the LICENSE.txt file.
#-----------------------------------------------------------------------------
import Pyro4.naming

#ns = Pyro4.naming.startNSloop(host='134.79.229.11')
ns = Pyro4.naming.startNSloop()

