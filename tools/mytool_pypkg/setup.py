import codecs

from pathlib import Path
from setuptools import setup

PKG_PATH = Path(__file__).parent

def readme():
    fname = PKG_PATH.joinpath('README.md')
    with codecs.open(fname, encoding='utf8') as fptr:
        return fptr.read()

def version():
    fname = PKG_PATH.joinpath('VERSION')
    with open(fname, 'r') as fptr:
        return fptr.read().strip()

reqs_list = ['nose', 'numpy', 'h5py', 'pandas', 'seaborn']

pkg_dict = {'mytool': ['PkgData/*', 'TestData/*']}

setup(
    name='mytool',
    version=version(),
    author='Jared J. Jared',
    author_email='jared@jared.org',
    maintainer='Jared J. Jared',
    maintainer_email='jared@jared.edu', 
    packages=['mytool'],
    package_data=pkg_dict, 
    url='http://fantastic.mytool.gov',
    license="It's not a real package",
    description="No really, it's not a real package",
    long_description=readme(),
    setup_requires=['nose>=1.0'],
    install_requires=reqs_list,
    tests_require=['nose>=1.0'],
    test_suite='mytool.test_suite',
    keywords='mytool',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.4',  
        'Intended Audience :: Science/Research', 
        'Intended Audience :: System Administrators', 
        'Natural Language :: English', 
        'Operating System :: MacOS :: MacOS X', 
        'Operating System :: Microsoft :: Windows :: Windows 7', 
        'Operating System :: POSIX', 
        'Topic :: Scientific/Engineering', 
        'Topic :: System :: Monitoring']
)
