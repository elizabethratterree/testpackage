from setuptools import setup, find_packages
def run_setup():
    setup(
        name='testpackage',
        version='1.0.1',
        packages=['source','source.testpackage1'],
        download_url='https://github.com/elizabethratterree/testpackage',
        install_requires=[
            'testpackage @ git+https://github.com/elizabethratterree/testpackage.git'
        ],
    )
