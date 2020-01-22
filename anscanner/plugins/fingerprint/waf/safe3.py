#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def safe3(headers,content):
	_ = False
	for header in headers.items():
		_ |= search(r'Safe3 Web Firewall|Safe3',header[1],I) is not None
		_ |= search(r'Safe3WAF',header[1],I) is not None
		if _:break
	if _ : 
		return "Safe3 Web Application Firewall"