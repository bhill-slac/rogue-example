# 
# ----------------------------------------------------------------------------
# Title      : rogue_example makefile
# ----------------------------------------------------------------------------
# File       : Makefile
# Author     : Ryan Herbst, rherbst@slac.stanford.edu
# Created    : 2016-10-23
# Last update: 2016-10-23
# ----------------------------------------------------------------------------
# Description:
# rogue_example makefile
# ----------------------------------------------------------------------------
# This file is part of the rogue_example software. It is subject to 
# the license terms in the LICENSE.txt file found in the top-level directory 
# of this distribution and at: 
#    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html. 
# No part of the rogue_example software, including this file, may be 
# copied, modified, propagated, or distributed except according to the terms 
# contained in the LICENSE.txt file.
# ----------------------------------------------------------------------------
# 

# Variables
CC       := g++
DEF      :=
CFLAGS   := -Wall `python3-config --cflags | sed s/-Wstrict-prototypes//` -fno-strict-aliasing
CFLAGS   += -I$(BOOST_PATH)/include -I$(ROGUE_DIR)/include -std=c++0x -fPIC
LFLAGS   := -lrogue -L$(ROGUE_DIR)/lib
BIN      := $(PWD)/bin

# Sources
APP_DIR := $(PWD)/src
APP_SRC := $(wildcard $(APP_DIR)/*.cpp)
APP_BIN := $(patsubst $(APP_DIR)/%.cpp,$(BIN)/%,$(APP_SRC))

# Targets
all: $(APP_BIN)

# Clean
clean:
	@rm -f $(BIN)/*

# Compile Shared Library
$(BIN)/%: $(APP_DIR)/%.cpp
	@test -d $(BIN) || mkdir $(BIN)
	@echo "Creating $@"; $(CC) $(CFLAGS) $(LFLAGS) -o $@ $<

