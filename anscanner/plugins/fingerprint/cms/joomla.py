#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt'

from re import search,I 

def joomla(headers,content):
	_  = False
	if 'set-cookie' in headers.keys():
		_ |= search(r"mosvisitor=",headers["set-cookie"],I) is not None
	_ |= search(r"\<meta name\=\"Generator\" content\=\"Joomla! - Copyright \(C\) 200[0-9] - 200[0-9] Open Source Matters. All rights reserved.\" \/\>",content) is not None
	_ |= search(r"\<meta name\=\"generator\" content\=\"Joomla! (\d\.\d) - Open Source Content Management\" \/\>",content) is not None
	_ |= search(r"Powered by \<a href\=\"http://www.joomla.org\"\>Joomla!\<\/a\>.",content) is not None
 	if _ : return "Joomla"