# Setup the same software environment used to build our binary.  By using
# "current", hopefully this important task is trivial.
#
# NOTE: If the gatekeepers change the "current" links after a build but before a
# job is executed, the binaries must be rebuilt.  Therefore, good and immediate
# communication about changes to "current" is important.
SETUP_SW_ENV=$MYSTUDY_DATA_CLONE/sites/bebop/setup_current_intel_mpich_stack.sh
ls -la $SETUP_SW_ENV
source $SETUP_SW_ENV
module list

In terms of logging its part of lab notes, we could write to the log file
* Start time
* End time
* git log of all repos involved in configuring & running job
* git diff of all repos involved in configuring & running job
* location of compilers as determined by PATH (e.g., which ifort)
* location of MPI wrapper
* location of HDF5 wrapper if used
* Mapping of computation to hardware (e.g., MPI and OpenMP setup)
* ls -lart of folder containing binary to get properties including size
* ldd of binary to view external dependencies and how they are satisfied in the
  execution environment.  For comparison with ldd output in build env.
* Print binary's version header
* All relevant environment variables

# Set read-only permissions to all data files and log files where possible.

