This python package is a minimal stand-in for an in-house data analysis tool.
It's main use is that we run its unit tests in an example data analysis Jupyter
notebook as part of logging important notes.

To install, setup/activate a virtual environment and execute
```
$ cd /path/to/lab-environment-2022-08-11-atpesc/tools/mytool_pypkg
$ python -m pip install build
$ python -m build
$ python -m pip install dist/mytool-4.3.2-py3-none-any.whl
```

To test your installation, from your virtual environment run
```
$ cd /path/to/lab-environment-2022-08-11-atpesc
$ ./tools/test_mytool_installation.py
```

To run the different jupyter notebooks, please execute the following in the
same virtual environment
```
$ python -m pip install jupyterlab
$ cd /path/to/lab-environment-2022-08-11-atpesc
$ jupyter lab
```
