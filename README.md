# rogue_example
Example project for rogue

The rogue project can be found at:

https://github.com/slaclab/rogue

To checkout rogue submodule:

> git submodule init
> git sudmodule update

See rogue/Readme files for rogue build instructions.

To build this example software you must first setup the environment. A
template file setup_template.csh is provided as an example. To 
use this file execute the following in your tcsh:

> source setup_template.csh

An RCE version is available as well

> source setup_rce.csh

If using a different shell the equivelent setup file for that shell 
must be created.

Once the environment is setup you can build this software:
> make

