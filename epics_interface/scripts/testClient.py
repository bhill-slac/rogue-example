#!/usr/bin/env python3

import epics

p = epics.PV('test.xxx')
print(p.get())
