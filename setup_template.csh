
# Python 3 support
source /afs/slac.stanford.edu/g/reseng/python/3.6.1/settings.csh
source /afs/slac.stanford.edu/g/reseng/boost/1.64.0/settings.csh

source /afs/slac.stanford.edu/g/reseng/zeromq/4.2.1/settings.csh
source /afs/slac.stanford.edu/g/reseng/epics/base-R3-16-0/settings.csh

# Package directories
setenv SURF_DIR   ${PWD}/../surf
setenv ROGUE_DIR  ${PWD}/../rogue

# Setup python path
setenv PYTHONPATH ${SURF_DIR}/python:${ROGUE_DIR}/python:${PYTHONPATH}

