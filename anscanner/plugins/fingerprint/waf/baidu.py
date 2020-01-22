#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I

def baidu(headers,content):
	_ = False
	for header in headers.items():
		_ |= search(r'fh1|yunjiasu-nginx',header[1],I) is not None
		if _ : break
	if _ :
		return "Yunjiasu Web Application Firewall (Baidu)" 