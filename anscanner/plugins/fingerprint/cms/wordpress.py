#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt'

from re import search,I 

def wordpress(headers,content):
	_  = False
	_ |= search(r"\<meta name\=\"generator\" content\=\"WordPress.com\" \/\>",content) is not None
	_ |= search(r"\<a href\=\"http://www.wordpress.com\"\>Powered by WordPress\<\/a\>",content) is not None
	_ |= search(r"\<link rel\=\'https://api.w.org/\'",content) is not None
	_ |= search(r"\/wp-content\/plugins\/",content) is not None
 	if _ : return "WordPress"