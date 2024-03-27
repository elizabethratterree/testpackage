from setuptools import setup, find_packages

setup(
    name='testpackage',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/elizabethratterree/testpackage',
    dependency_links=[
        'git+https://github.com/elizabethratterree/testpackage.git#egg=testpackage-1.0.0'
    ],
    install_requires=[
        # List your dependencies here
    ],
)