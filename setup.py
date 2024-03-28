from setuptools import setup, find_packages

setup(
    name='testpackage',
    version='1.0.0',
    packages=find_packages(),
    package_data={'testpackage': ['source/testpackage/*']},
    url='https://github.com/elizabethratterree/testpackage',
    install_requires=[
        'testpackage @ git+https://github.com/elizabethratterree/testpackage.git'
    ],
)
