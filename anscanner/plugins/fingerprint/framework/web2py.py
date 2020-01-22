#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I

def web2py(headers,content):
	_ = False
	for header in headers.items():
		_ |= search("web2py",header[1]) is not None
		if _ : break
	_ |= search(r"\<div id\=\"serendipityLeftSideBar\"\>",content) is not None
	if _ : return "Web2Py - Python Framework"