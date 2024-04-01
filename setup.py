from setuptools import setup

from testpackage1 import __version__

setup(
    name='testpackage1',
    version=__version__,

    url='https://github.com/elizabethratterree/testpackage',
    author='Elizabeth Ratterree',
    author_email='elizabeth.ratterree@my.utsa.edu',

    py_modules=['testpackage1'],
)
