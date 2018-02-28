# Rogue C++ RSSI Data Receiver

This directory contains an example of created a RSSI / packetizer data receiver purely in C++

The current example hard codes the IP address and port number within the C++ file. Edit this file to match your data generator.

## Building the example

First setup the rogue environment:

````
$ source /path/to/rogue/setup_rogue.sh
```
or
````
$ source /path/to/rogue/setup_rogue.csh
```

The example project uses cmake which will automatically generate a
makefile to properly link this example against rogue, boost and python3.

````
$ mkdir build
$ cd build
$ cmake ..
$ make
````

### Running the example

The executable can be found in bin/rssi_sink

````
$ bin/rssi_sink
````

