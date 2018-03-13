# rogue-example

A repository containing example usages for rogue.

The main rogue repository can be found at:

https://github.com/slaclab/rogue

## Sub Directories

### cpp_api

Example c++ sources and python trees demonstrating the C++ API wrapper which allows 
a rougue python tree to be integrated into a C++ software package.

### custom_python_module

Example C++ project for creating a custom rogue module which can be integrated into a pyrogue project. 

### custom_stream_receivers

An example of a pure c++ udp/rssi/packetizer receiver as well as some python stream receiver examples.

### epics_interface

Example of setting up an epics interface with a streaming source and destination.

### example_devices

This sub-directory contains examples of device, variable and command creation.

### file_writer_test

Example test script for reading and write files with and without compression.

### shared_mem_client

Example of controlling a pyrogue tree through a shared memory interface

### stream_testers

PRBS RX/TX scripts with various levels of packetizer and RSSI support with UDP tests as well.

### scripts

This is a legacy sub-directory which will be emptied out as examples are moved into individual sub-directories.
