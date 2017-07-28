#!/usr/bin/env python
# coding: utf-8

"""
    distutils setup
    ~~~~~~~~~~~~~~~

    :homepage: https://github.com/mastahyeti/gping/
    :copyleft: 1989-2011 by the python-ping team, see AUTHORS for more details.
    :license: GNU GPL v2, see LICENSE for more details.
"""

import os

from setuptools import setup, find_packages, Command

def get_authors():
    authors = []
    try:
        f = file(os.path.join(PACKAGE_ROOT, "AUTHORS"), "r")
        for line in f:
            if not line.strip().startswith("*"):
                continue
            if "--" in line:
                line = line.split("--", 1)[0]
            authors.append(line.strip(" *\r\n"))
        f.close()
        authors.sort()
    except Exception, err:
        authors = "[Error: %s]" % err
    return authors


setup(
    name='gping',
    version="0.2",
    description='A gevent fork of python-ping.',
    author=get_authors(),
    maintainer="Ben Toews",
    maintainer_email="mastahyeti@gmail.com",
    url='https://github.com/mastahyeti/gping',
    keywords="ping icmp network latency gevent",
    py_modules=['gping'],
    install_requires=['gevent', 'args'],
    dependency_links=[
        'https://github.com/kennethreitz/args/tarball/0a6d5eb#egg=args',
    ],
    entry_points={
        'console_scripts': [
            'gping = gping:run',
        ],
    },
)
