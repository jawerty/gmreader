#!/usr/bin/env python

from setuptools import setup

setup(
      name='gmreader',
      version='0.1.5',
      description='Let python read your google emails to you. Listen to your gmails instead of reading them',
      author='Jared Wright',
      license='MIT',
      keywords = "email gmail google mail read text to speech",
      author_email='jawerty210@gmail.com',
      url='http://github.com/jawerty/gmreader',
      scripts=['gmreader.py'],
      install_requires=['BeautifulSoup'],
      entry_points = {
        'console_scripts': [
            'gmreader = gmreader:main'
        ],
	    }
     )