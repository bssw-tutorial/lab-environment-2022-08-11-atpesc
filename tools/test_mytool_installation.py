#!/usr/bin/env python

"""
Run the script with -h to obtain more information regarding the script.
"""

import sys
import argparse

import subprocess as sbp

# ----- HARDCODED VALUES
# Exit codes so that this can be used in CI build server
_FAILURE = 1
_SUCCESS = 0


try:
    import mytool
except ImportError as error:
    print()
    print(f"ERROR: {error.name} Python package not installed")
    print()
    exit(_FAILURE)


def main():
    # Keep output compact so that package info is seen with each run
    DEFAULT_VERBOSITY = 1

    # ----- SPECIFY COMMAND LINE USAGE
    DESCRIPTION = "Print mytool Python package installation information " \
                  "and run full\ntest suite on installation.\n\n" \
                  "A zero exit code indicates success.  " \
                  "Nonzero exit codes indicate failure."
    VERBOSE_HELP = "Verbosity level of Python unittest logging"
    parser = argparse.ArgumentParser(
                description=DESCRIPTION,
                formatter_class=argparse.RawTextHelpFormatter
             )
    parser.add_argument(
        "--verbose", "-v",
        type=int, choices=[0, 1, 2], default=DEFAULT_VERBOSITY,
        help=VERBOSE_HELP
    )

    # ----- GET COMMAND LINE ARGUMENTS
    args = parser.parse_args()
    verbosity_level = args.verbose

    # ----- PRINT VERSION INFORMATION
    print()
    sbp.run(["pip", "show", "mytool"])
    print()
    sys.stdout.flush()

    # ----- RUN FULL TEST SUITE
    return _SUCCESS if mytool.test(verbosity_level) else _FAILURE


if __name__ == "__main__":
    exit(main())
