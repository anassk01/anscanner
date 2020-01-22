#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def mac(headers):
	for header in headers.items():
		if search(r'^mac|^macos',header[1],I):
			return "MacOS"