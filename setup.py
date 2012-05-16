# Copyright (C) 2009, 2010 Robert Lehmann
# Python 3 support via 2to3 added by Phillip Alday

from setuptools import setup
import os.path

setup(name='libleipzig',
      version='1.4',
      description='wortschatz.uni-leipzig.de binding',
      long_description=open(os.path.join(os.path.dirname(__file__),
          'README.rst')).read(),
      url='http://github.com/palday/libleipzig-python/',
      setup_requires=['distribute'],
      install_requires = ['suds'],
      tests_require = ['nose'],
      test_suite = 'nose.collector',
      author='Robert Lehmann',
      author_email='libleipzig@robertlehmann.de',
      maintainer='Phillip Alday',
      maintainer_email='phillip.alday@staff.uni-marburg.de',
      license='GPLv3',
      packages=['libleipzig', 'libleipzig.test'],
      package_dir={'libleipzig.test': 'tests'},
      package_data={'libleipzig': ['README.rst', 'manual.html']},
      entry_points={'console_scripts': ['wortschatz = libleipzig.main:main']},
      zip_safe=True,
      use_2to3 = True,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Natural Language :: German',
          'Topic :: Text Processing :: Linguistic',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.4',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.0',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
        ],
      
       # PEP-314 states that if possible license & plaform should be specified
       # using 'classifiers'.
       platforms=['(specified using classifiers)'],
)
