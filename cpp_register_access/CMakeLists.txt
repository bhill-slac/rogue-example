# ----------------------------------------------------------------------------
# Title      : ROGUE RSSI Receiver In C++
# ----------------------------------------------------------------------------
# File       : CMakeLists.txt
# Created    : 2018-02-27
# ----------------------------------------------------------------------------
# This file is part of the rogue_example software. It is subject to 
# the license terms in the LICENSE.txt file found in the top-level directory 
# of this distribution and at: 
#    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html. 
# No part of the rogue_example software, including this file, may be 
# copied, modified, propagated, or distributed except according to the terms 
# contained in the LICENSE.txt file.
# ----------------------------------------------------------------------------

# Add support for building in conda environment
if (DEFINED ENV{CONDA_PREFIX})
   set(CMAKE_PREFIX_PATH "$ENV{CONDA_PREFIX}")
   link_directories($ENV{CONDA_PREFIX}/lib)
endif()

# Check cmake version
cmake_minimum_required(VERSION 3.5)
include(InstallRequiredSystemLibraries)

# Project name
project (RssiReg)

# C/C++
enable_language(CXX)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wno-deprecated")
#add_definitions(-D__STDC_FORMAT_MACROS)

#####################################
# Find Rogue & Support Libraries
#####################################
if (DEFINED ENV{ROGUE_DIR})
   set(Rogue_DIR $ENV{ROGUE_DIR}/lib)
else()
   set(Rogue_DIR ${CMAKE_PREFIX_PATH}/lib)
endif()
find_package(Rogue)

#####################################
# EPICS
#####################################
if(DEFINED ENV{EPICS_HOST_ARCH})
   set(EPICSV3_ARCH      $ENV{EPICS_HOST_ARCH})
else()
   execute_process(COMMAND ${EPICSV3_BASE_DIR}/startup/EpicsHostArch 
				   OUTPUT_VARIABLE EPICSV3_ARCH OUTPUT_STRIP_TRAILING_WHITESPACE)
   string(REGEX REPLACE "\n$" "" EPICSV3_ARCH "${EPICSV3_ARCH}")
endif()

set(EPICSV3_LIB_DIR   ${EPICSV3_BASE_DIR}/lib/${EPICSV3_ARCH} )

if(DEFINED ENV{EPICS_PCAS_ROOT})
   set(EPICS_PCAS_ROOT   $ENV{EPICS_PCAS_ROOT})
   set(EPICSV3_INCLUDES  ${EPICS_PCAS_ROOT}/include
					     ${EPICSV3_BASE_DIR}/include
					     ${EPICSV3_BASE_DIR}/include/compiler/gcc 
					     ${EPICSV3_BASE_DIR}/include/os/Linux)

   set(EPICSV3_LIBRARIES ${EPICS_PCAS_ROOT}/lib/$ENV{EPICS_HOST_ARCH}/libcas.so 
					     ${EPICS_PCAS_ROOT}/lib/$ENV{EPICS_HOST_ARCH}/libgdd.so
					     ${EPICSV3_LIB_DIR}/libca.so 
					     ${EPICSV3_LIB_DIR}/libCom.so )
else()
   set(EPICSV3_INCLUDES  ${EPICSV3_BASE_DIR}/include
					     ${EPICSV3_BASE_DIR}/include/compiler/gcc 
					     ${EPICSV3_BASE_DIR}/include/os/Linux)

   set(EPICSV3_LIBRARIES ${EPICSV3_LIB_DIR}/libcas.so 
					     ${EPICSV3_LIB_DIR}/libca.so
					     ${EPICSV3_LIB_DIR}/libCom.so
					     ${EPICSV3_LIB_DIR}/libgdd.so )
endif()

#####################################
# Setup build
#####################################

# Include files
include_directories(${ROGUE_INCLUDE_DIRS})

# Set output directory
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)

# Compile each source
file(GLOB APP_SOURCES ${PROJECT_SOURCE_DIR}/src/*.cpp)
foreach (srcFile ${APP_SOURCES})
   get_filename_component(binName ${srcFile} NAME_WE)
   add_executable(${binName} ${srcFile})
   TARGET_LINK_LIBRARIES(${binName} LINK_PUBLIC ${ROGUE_LIBRARIES})
endforeach ()

