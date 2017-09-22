#! /usr/bin/env python
#
# Copyright (C) 2014-2017 Mikko Kotila

DESCRIPTION = "Logly"
LONG_DESCRIPTION = """\

Set of useful and battle tested tools for logfile analysis. Developed 
for use in Botlab's research analyzing exchange logfiles for ad fraud
studies. 

"""

DISTNAME = 'logly'
MAINTAINER = 'Mikko Kotila'
MAINTAINER_EMAIL = 'mailme@mikkokotila.com'
URL = 'http://botlab.io'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/botlabio/logly/'
VERSION = '0.6'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup


def check_dependencies():

    install_requires = []

    try:
        import netaddr
    except ImportError:
        install_requires.append('netaddr')
    try:
        import numpy
    except ImportError:
        install_requires.append('numpy')
    try:
        import pandas
    except ImportError:
        install_requires.append('pandas')

    return install_requires

if __name__ == "__main__":

    install_requires = check_dependencies()

    setup(name=DISTNAME,
          author=MAINTAINER,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          install_requires=install_requires,
          packages=['logly'],

          classifiers=[
              'Intended Audience :: Science/Research',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3.5',
              'License :: OSI Approved :: MIT License',
              'Topic :: Security',
              'Topic :: Internet :: Log Analysis',
              'Operating System :: POSIX',
              'Operating System :: Unix',
              'Operating System :: MacOS'])
