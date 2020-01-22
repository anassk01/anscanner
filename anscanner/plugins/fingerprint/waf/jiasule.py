#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def jiasule(headers,content):
	_ = False
	for header in headers.items():
		_ |= search(r'__jsluid=|jsl_tracking',header[1],I) is not None
		_ |= search(r'jiasule-waf',header[1],I) is not None
		if _:break
	_ |= search(r'static\.jiasule\.com/static/js/http_error\.js',content) is not None
	if _ : 
		return "Jiasule Web Application Firewall (Jiasule)"