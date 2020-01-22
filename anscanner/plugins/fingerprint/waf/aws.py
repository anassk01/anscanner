#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I

def aws(headers,content):
	_ = False
	for header in headers.items():
		_ |= search(r'\bAWS',header[1],I) is not None
	if _: 
		return "Amazon Web Services Web Application Firewall (Amazon)" 