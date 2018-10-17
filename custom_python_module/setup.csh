
if ( ! $?PYTHONPATH ) then
   setenv PYTHONPATH ""
endif

# Setup python path
setenv PYTHONPATH ${PWD}/python:${PYTHONPATH}

