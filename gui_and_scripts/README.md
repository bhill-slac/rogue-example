# Script and GUI examples
This directory includes examples for using the GUI and scripts both localy and with remote clients.

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

## Running a GUI/Server combination

Run the gui/server test script

````
$ python3 scripts/serverGui.py
````

## Adding a second GUI client

In another window setup the environent and connect a GUI remotely

````
$ python3 scripts/guiClient.py
````

You can various settings in the GUI observe how they change in the other GUI

## Running a script client

You can try running a script in another window session and ovserve the changes in the other two GUIs

````
$ ipython3 -i scripts/scriptClient.py
In [1]: dummyTree.AxiVersion.ScratchPad.set(0x55)
````

You can interact with the tree directly and observe the changes. You can also run the script in a non-interactive way.

````
$ python scripts/scriptClient.py
````

## Other Scripts

You can interact with the tree in the server session.

````
$ ipython3 -i scripts/scriptOnly.py
In [1]: dummyTree.AxiVersion.ScratchPad.set(0x55)
In [2]: dummyTree.AxiVersion.ScratchPad.get()
````

You can start a server without an attached GUI and try connecting remote GUIs and script clients to it

````
$ python3 scripts/serverOnly.py
````

You can also start a standalone pyro4 nameserver and use it instead of the pyrogue root server

````
$ python3 scripts/startPyro4Ns.py
````
