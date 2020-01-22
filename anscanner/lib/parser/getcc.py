#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

import re

def getcc(content):
	"""Credit Card"""
	CC_LIST = re.findall(r'((^|\s)\d{4}[- ]?(\d{4}[- ]?\d{4}|\d{6})[- ]?(\d{5}|\d{4})($|\s))',content)
	if CC_LIST != None or CC_LIST != []:
		return CC_LIST