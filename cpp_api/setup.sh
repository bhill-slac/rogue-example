

if [ -z "$PYTHONPATH" ]
then
   PYTHONPATH=""
fi

# Setup python path
export PYTHONPATH=${PWD}/scripts:${PWD}/../example_devices:${PYTHONPATH}

