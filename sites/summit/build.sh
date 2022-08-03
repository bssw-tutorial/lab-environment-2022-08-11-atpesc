# Setup software environment using "current" setup scripts in data clone that
# are maintained and tested by the gatekeepers.
#
# NOTE: If this is changed, then similar changes might need to be made in
# associated job scripts.
SETUP_SW_ENV=$MYSTUDY_DATA_CLONE/sites/summit/setup_current_nvhpc_mpich_stack.sh
ls -la $SETUP_SW_ENV
source $SETUP_SW_ENV
module list

See build.sh for Bebop for more info.

