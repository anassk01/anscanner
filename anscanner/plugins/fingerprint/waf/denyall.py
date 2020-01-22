#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I

def denyall(headers,content):
	_ = False
	for header in headers.items():
		_ |= search(r'sessioncookie=',header[1],I) is not None
		if _: break
	_ |= search(r"Condition Intercepted",content) is not None
	if _ :
		return "Deny All Web Application Firewall (DenyAll)"