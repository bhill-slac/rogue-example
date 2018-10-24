
# In case python path is not set
if [ -z "$PYTHONPATH" ]
then
   PYTHONPATH=""
fi

# Current directory
LOC_DIR=$(dirname -- "$(readlink -f ${BASH_SOURCE[0]})")

# Update python path
export PYTHONPATH=${LOC_DIR}/scripts:${LOC_DIR}/../example_devices:${PYTHONPATH}


