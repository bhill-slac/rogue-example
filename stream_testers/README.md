#  PRBS Test Scripts

This directory contains a test script for creating a udp server and connecting at client to it.

Once connected a PRBS stream will be sent from the client to the server.

This scripts tests a number of modules as well as testing the frame buffer structures.

## Runing the tests

First setup the rogue environment:

````
$ source /path/to/rogue/setup_rogue.sh
````

or

````
$ source /path/to/rogue/setup_rogue.csh
````
Once the environment is setup you can run the tests

PRBS to PRBS simple test

````
$ python3 scripts/prbsTest.py
````

Add the packetizer V1

````
$ python3 scripts/packetizerV1Test.py
````

Add the packetizer V2

````
$ python3 scripts/packetizerV1Test.py
````

Add RSSI with packetizer V1

````
$ python3 scripts/rssiTest.py
````

UDP/RSSI/Packetizer V1

````
$ python3 scripts/udpPacketizerV1.py
````

UDP/RSSI/Packetizer V2

````
$ python3 scripts/udpPacketizerV1.py
````

