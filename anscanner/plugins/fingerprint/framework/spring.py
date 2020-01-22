#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I

def spring(headers,content):
	_ = False
	for header in headers:
		_ |= search("org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=",header[1])is not None
		if _: break 
	if _: return "Spring Framework (Java Platform)"