# -*- coding: utf-8 -*-
# (c) 2015 Jose Zambudio Bernabeu - Zamberjo
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html


import os
import re
import openerp
from distutils.dir_util import copy_tree

print "Copying telegram python package on odoo root folder..."

import pdb; pdb.set_trace()
fromDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'telegram')
toDirectory = os.path.join(os.path.dirname(openerp.__file__), 'service')

with open(os.path.join(toDirectory, '__init__.py'), "r") as sources:
    lines = sources.readlines()
with open(os.path.join(toDirectory, '__init__.py'), "w") as sources:
    for line in lines:
        sources.write(line)
        if line.strip() == 'import server':
            sources.write("import telegram\n")

copy_tree(fromDirectory, toDirectory)
