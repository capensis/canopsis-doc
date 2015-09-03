#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

BASE_URL = 'https://git.canopsis.net/canopsis/canopsis-doc'
GIT_URL = '{0}.git'.format(BASE_URL)
DL_URL = '{0}/repository/archive.tar.gz?ref=v0.1a'.format(BASE_URL)


setup(
    name='cpsdocgen',
    version='0.1a',
    license='MIT',

    author='Capensis',
    author_email='contact@capensis.fr',
    description='Canopsis Documentation Generator',
    url=GIT_URL,
    download_url=DL_URL,
    keywords=['canopsis', 'documentation', 'generator'],
    classifiers=[],

    scripts=['scripts/cpsdocgen'],
    packages=find_packages(),
    install_requires=[
        'argparse>=1.2.1',
        'jinja2>=2.7.3',
        'pygit2>=0.22.1',
        'Sphinx>=1.3.1'
    ]
)
