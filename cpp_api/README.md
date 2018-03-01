# Rogue C++ API Examples

This directory contains an example of using the C++ api to access pyrogue trees from a C++ program. Both a local and remote example are included.

The local example starts a tree directly, acting the the local server for the tree.

The remote example connects to a remote tree using the pyro4 interface.

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

There will now be two output files in the bin directory.

### Setting up the environment

To use this example you will need to add the example_devices directory to your python path. A local setup script will properly example_devices directory to your python path.

````
$ source setup.sh
````
or
````
$ source setup.csh
````

### Running the examples

First start the local example which will create an instance of the DummyRoot python tree which is described in the scripts/testApi.py file. This program will start the tree, write and read a scratchpad register and then dump a list of variables and commands from the tree structure.

````
$ bin/api_local
````

To run the remote test you will need two windows, both with the appropriate rogue and local environment setup. In the first window you will start a python instance of the DummyTree and run it in a while loop.

````
$ python3 scripts/testApi.py
````

In the second window you will start a C++ client which will attach to the Rogue tree and perform the same test and dump opeations.

````
$ bin/api_remote
````

