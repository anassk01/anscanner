#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/anassk01/anscanner/blob/master/anscanner/
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt

from re import search,I

def cherrypy(headers,content):
	_ = False
	for header in headers.items():
		_ |= search("CherryPy",header[1]) is not None
		if _ : break
	if _ : return "CherryPy - Python Framework"