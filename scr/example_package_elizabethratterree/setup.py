from setuptools import setup

from my_pip_package import __version__

setup(
    name='my_pip_package',
    version=__version__,

    url='https://github.com/elizabethratterree/testpackage.git',
    author='Elizabeth Ratterree',
    author_email='elizabeth.ratterree@my.utsa.edu',

    py_modules=['my_pip_package'],
)
