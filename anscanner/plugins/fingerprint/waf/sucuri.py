#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def sucuri(headers,content):
	_ = False
	_ |= search(r"Questions\?.+cloudproxy@sucuri\.net",content) is not None
	_ |= search(r"Sucuri WebSite Firewall - CloudProxy - Access Denied",content) is not None
	_ |= search('sucuri/cloudproxy',str(headers.values()),I) is not None
	if _ : 
		return "CloudProxy WebSite Firewall (Sucuri)"