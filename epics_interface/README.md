# EPICS Interface Example
This directory includes an example of setting up an epics interface.

## Using the scripts

First setup the rogue environment:

````
$ source /path/to/rogue/setup_rogue.sh
````
or
````
$ source /path/to/rogue/setup_rogue.csh
````
Source the local setup script to add the example devices to your PYTHONPATH variable.

````
$ source setup.sh
````
or
````
$ source setup.csh
````

You can now run the test script:

````
$ python3 scripts/testServer.py
````

You can use EPICS commands to set and monitor variables being monitored and updated.

Test the scratchpad

````
$ caput test:dummyTree:AxiVersion:ScratchPad 200
$ caget test:dummyTree:AxiVersion:ScratchPad
````

One variable is setup as a list variable, Try setting it and monitoring its updates.

````
$ caput -a test:dummyTree:listVar 10 1 2 3 4 5 6 7 8 9 10
$ caget test:dummyTree:listVar
$ camonitor test:dummyTree:listVar
````

Test writing a reading a string.

````
$ caput -s test:dummyTree:strVar "This is a test"
$ caget test:dummyTree:strVar
````

Test pushing stream data to and from the server.

````
$ caput -a test:dummyTree:mast 20 1 2 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
$ camonitor test:dummyTree:slave 
````

