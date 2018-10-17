
if ( ! $?PYTHONPATH ) then
   setenv PYTHONPATH ""
endif

# Setup python path
setenv PYTHONPATH ${PWD}/scripts:${PWD}/../example_devices:${PYTHONPATH}

