#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This software is licensed under version 2.0 of the WTFPL (see COPYING for details)
"""

import sys
import os
import re
from models import *
from jinja2 import Environment, PackageLoader

def cleanify(name):
	''' Strip out some things that don't play well in element ids '''
	return re.sub(r"[\. ']", r'_', name)

# are we running this standalone, rather than as a module?
def main():
	# Check to see if we have all the information we need
	try:
		directory = unicode(sys.argv[1])
		#directory = sys.argv[1]
		template = sys.argv[2]
	except IndexError:
		print "Usage: " + sys.argv[0] + " <directory> <template>"
		exit()
	
	root = Folder(directory)
	root.scan()
	
	env = Environment(loader=PackageLoader('bxt_description_generator', 'templates'))
	env.filters['cleanify'] = cleanify
	template = env.get_template(template)
	print template.render(root=root).encode("utf-8")

if __name__ == '__main__':
	sys.exit(main())
