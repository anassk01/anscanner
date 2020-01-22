#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def varnish(headers,content):
	_ = False
	_ |= search(r'varnish|x-varnish',str(headers.values()),I) is not None
	if _ : 
		return "Varnish FireWall (OWASP)"