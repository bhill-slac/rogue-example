# File Writer Test

This directory contains a test script for creating a udp server and connecting at client to it.

Once connected a PRBS stream will be sent from the client to the server.

This scripts tests a number of modules as well as testing the frame buffer structures.

## Runing the test

First setup the rogue environment:

````
$ source /path/to/rogue/setup_rogue.sh
````

or

````
$ source /path/to/rogue/setup_rogue.csh
````
Once the environment is setup you can run the test

````
$ python3 scripts/udpPacketizerV1.py
````

