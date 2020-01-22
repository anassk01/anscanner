#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def radware(headers,content):
	_ = False
	for header in headers.items():
		_ |= header[0] == "x-sl-compstate"
		if _:break
	_ |= search(r'Unauthorized Activity Has Been Detected.+Case Number:',content) is not None
	if _ : 
		return "AppWall (Radware)"