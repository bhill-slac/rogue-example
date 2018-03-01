# Rogue Shared Memory Example

This directory contains an example of using the shared memory interface to control and monitor a pyrogue tree.

## Building the examples

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

### Setting up the environment

To use this example you will need to add the example_devices directory to your python path. A local setup script will properly example_devices directory to your python path.

````
$ source setup.sh
````
or
````
$ source setup.csh
````

### Running the example

To test the shared memory interface you will need two windows, both with the appropriate rogue and local environment setup. In the first window you will start a python instance of the DummyTree and run it in a while loop.

````
$ python3 scripts/testSmem.py
````

In the second window you will start a C++ client which will attach to shared memory interface to write and read a scratchpad register.

````
$ bin/smem_test
````

