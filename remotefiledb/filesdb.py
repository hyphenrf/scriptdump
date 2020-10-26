#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
"""
This script emulates the structure of PISI files.db database for seamless
injection of new entries.
"""

from shelve import open as dbopen
from hashlib import md5
import os

filesdb = {}
workdir = '/tmp/lists'

packages = os.listdir(workdir)
for package in packages:
    packagepath = "%s/%s" %(workdir, package)
    with open(packagepath, 'r') as fd:
        name = fd.readline().strip()
        filesdb.update(
            { md5(path.strip()[1:]).digest(): name for path in fd }
        )

db = dbopen("files.db")
db.update(filesdb)
db.close()
