# Setup software environment using "current" setup scripts in data clone that
# are maintained and tested by the gatekeepers.
#
# NOTE: If this is changed, then similar changes might need to be made in
# associated job scripts.
SETUP_SW_ENV=$MYSTUDY_DATA_CLONE/sites/bebop/setup_current_intel_mpich_stack.sh
ls -la $SETUP_SW_ENV
source $SETUP_SW_ENV
module list

In terms of logging its part of lab notes, we could write to the log file
* Start time
* End time
* git log of all repos involved in build
* git diff of all repos involved in build
* location of compilers as determined by PATH (e.g., which ifort)
* compiler versions
* location of MPI wrapper
* MPI wrapper contents (e.g., mpif90 -show)
* location of HDF5 wrapper if used
* HDF5 wrapper contents (e.g., h5pfc -show)
* ls -lart of folder containing binary to get properties including size
* ldd of binary to view external dependencies and how they are satisfied in the
  build environment.  For comparison with ldd output in job env.
* Print binary's version header
* All relevant environment variables

