#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def urlscan(headers,content):
	_ = False
	_ |= search('rejected-by-urlscan',str(headers.values()),I) is not None
	_ |= search(r'Rejected-By-UrlScan',content,I) is not None
	if _ : 
		return "UrlScan (Microsoft)"