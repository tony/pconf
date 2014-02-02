# -*- coding: utf-8 -*-
"""Tests for pconf.

testsuite.pconf
---------------

"""

from __future__ import absolute_import, division, print_function, \
    with_statement, unicode_literals

import os
import tempfile
import logging
import unittest
import zipfile
import shutil


log = logging.getLogger(__name__)


def suite():
    suite = unittest.TestSuite()
    #suite.addTest(unittest.makeSuite(UtilTestCase))
    return suite
