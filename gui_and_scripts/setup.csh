
# In case python path is not set
if ( ! $?PYTHONPATH ) then
   setenv PYTHONPATH ""
endif

# Set current directory
set CMD=($_)
set LOC_PATH=`readlink -f "$CMD[2]"`
set LOC_DIR=`dirname "$LOC_PATH"`

# Update python path
setenv PYTHONPATH ${LOC_DIR}/scripts:${LOC_DIR}/../example_devices:${PYTHONPATH}

