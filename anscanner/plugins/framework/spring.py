#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/anassk01/anscanner/blob/master/anscanner/
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt

from re import search,I

def spring(headers,content):
	_ = False
	for header in headers:
		_ |= search("org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=",header[1])is not None
		if _: break 
	if _: return "Spring Framework (Java Platform)"