# Custom Rogue Python Module Example
This directory includes an example of building your own rogue module which can be included in 
a pyrogue script. This example module creates a rogue stream receiver which can 
receive and process data. The example script connects this example module to a 
prbs generator.

## Building the module

First setup the rogue environment:

````
$ source /path/to/rogue/setup_rogue.sh
````
or
````
$ source /path/to/rogue/setup_rogue.csh
````
The example project uses cmake which will automatically generate a
makefile to properly link this example against rogue, boost and python3.

````
$ mkdir build
$ cd build
$ cmake ..
$ make
````

Once the module is built it will generate a library file in the lib sub-directory. Source
the local setup script to add this path to your PYTHONPATH variable.

````
$ source setup.sh
````
or
````
$ source setup.csh
````

You can now run the test script:

````
$ python3 scripts/testMyModule.py
````

