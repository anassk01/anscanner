#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

import re

def getmail(content):
	"""E-mail"""
	EMAIL_LIST = re.findall(r'[a-zA-Z0-9.\-_+#~!$&\',;=:]+@+[a-zA-Z0-9-]*\.\w*',content)
	if EMAIL_LIST != None or EMAIL_LIST != []:
		return EMAIL_LIST