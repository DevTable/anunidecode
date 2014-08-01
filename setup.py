import sys

try:
    from setuptools import setup
except ImportError:
    from distutils import setup

readme = open('README.rst', 'r')
README_TEXT = readme.read()
readme.close()

setup(
    name='anunidecode',
    version='0.01',
    description='Another translation of the unidecode module created by Sean M. Burke opting to retain the perl license.',
    long_description=README_TEXT,
    author='Jake Moshenko',
    author_email='jake@devtable.com',
    url='https://github.com/DevTable/anunidecode',
    packages=['anunidecode'],
    package_dir={
        'anunidecode' : 'anunidecode',
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Perl License'
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
