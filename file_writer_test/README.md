# File Writer Test

This directory contains a python test script which writes PRBS data to a file and then reads that data back.

This example also uses the compress / uncompress modules.

## Runing the test

First setup the rogue environment:

````
$ source /path/to/rogue/setup_rogue.sh
````

or

````
$ source /path/to/rogue/setup_rogue.csh
````
Once the environment is setup you can run the file writer test

````
$ python3 scripts/fileTest.py
````

The max size for each file can be set in the following line:

````
fwr.setMaxSize(1000003)
````

If this value is non zero multiple data files will be created.

A version of the script which uses compression is also available.

````
$ python3 scripts/fileTest.py
````

