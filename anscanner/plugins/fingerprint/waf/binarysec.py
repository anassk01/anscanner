#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I

def binarysec(headers,content):
	_ = False
	for header in headers.items():
		_ |=  header[0].lower() == "x-binarysec-via"
		_ |=  header[0].lower() == "x-binarysec-nocache"
		_ |= search(r'binarySec',header[1],I) is not None
		if _: break
	if _ : 
		return "BinarySEC Web Application Firewall (BinarySEC)"