# -*- coding: utf-8 -*-

version = '2.20.0.2.dev0'

from setuptools import setup, find_packages

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(name='collective.js.fancytree',
      version=version,
      description='Fancytree as a zope resource',
      long_description=long_description,
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Plone :: Addon",
          "Framework :: Plone :: 6.0",
          "Framework :: Plone :: 6.1",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
          "Operating System :: OS Independent",
          "Programming Language :: JavaScript",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
          "Programming Language :: Python :: 3.11",
          "Programming Language :: Python :: 3.12",
          "Programming Language :: Python :: 3.13",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='',
      author='IMIO',
      author_email='support@imio.be',
      url='https://github.com/imio/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'collective.js.jqueryui'
      ],
      extras_require={
          'test': [
              'plone.app.testing',
          ]
      },
      entry_points={},
      )
