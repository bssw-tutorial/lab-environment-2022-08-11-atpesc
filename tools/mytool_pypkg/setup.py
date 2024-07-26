import codecs

from pathlib import Path
from setuptools import setup

_PKG_ROOT = Path(__file__).parent.resolve()
_GH_ADDRESS = "https://github.com/bssw-tutorial/lab-environment-2022-08-11-atpesc"


def readme_md():
    fname = _PKG_ROOT.joinpath("README.md")
    with codecs.open(fname, encoding="utf8") as fptr:
        return fptr.read()


def version():
    fname = _PKG_ROOT.joinpath("VERSION")
    with open(fname, "r") as fptr:
        return fptr.read().strip()


# Changes made to python_requires should be propagated to all GitHub Action
# config files.
python_requires = ">=3.9"
code_requires = ["h5py", "numpy", "scipy", "pandas", "seaborn"]
test_requires = []
install_requires = code_requires + test_requires

package_data = {
    "mytool": ["PkgData/*", "tests/TestData/*"]
}

project_urls = {
    "Source": _GH_ADDRESS,
    "Documentation": _GH_ADDRESS,
    "Tracker": f"{_GH_ADDRESS}/issues",
}

setup(
    name="mytool",
    version=version(),
    author="Jared J. Jared",
    author_email="jared@jared.org",
    maintainer="Jared J. Jared",
    maintainer_email="jared@jared.edu", 
    package_dir={"": "src"},
    package_data=package_data, 
    url="http://fantastic.mytool.gov",
    project_urls=project_urls,
    license="It's not a real package",
    description="No really, it's not a real package",
    long_description=readme_md(),
    long_description_content_type="text/markdown",
    python_requires=python_requires,
    install_requires=install_requires,
    keywords="mytool",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research", 
        "Intended Audience :: System Administrators", 
        "Natural Language :: English", 
        "Operating System :: MacOS :: MacOS X", 
        "Operating System :: Microsoft :: Windows :: Windows 7", 
        "Operating System :: POSIX", 
        "Topic :: Scientific/Engineering", 
        "Topic :: System :: Monitoring"]
)
