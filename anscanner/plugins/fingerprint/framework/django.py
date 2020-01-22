#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I

def django(headers,content):
	_ = False
	for header in headers.items():
		_ |= search("wsgiserver/",header[1]) is not None
		_ |= search("python/",header[1]) is not None
		_ |= search("csrftoken=",header[1]) is not None
		if _ : break
	_ |= search(r"\<meta name\=\"robots\" content\=\"NONE,NOARCHIVE\"\>\<title\>Welcome to Django\<\/title\>",content) is not None 
	if _ : return "Django - Python Framework"