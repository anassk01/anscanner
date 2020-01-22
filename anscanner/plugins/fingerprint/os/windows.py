#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def windows(headers):
	os = ["windows","win32"]
	for o in os:
		for header in headers.items():
			if search(o,header[1],I):
				return o.title()