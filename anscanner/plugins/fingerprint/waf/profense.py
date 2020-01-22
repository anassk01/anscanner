#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def profense(headers,content):
	_ = False
	for header in headers.items():
		_ |= search(r'profense',header[1],I) is not None
		_ |= search(r'PLBSID=',header[1],I) is not None
		if _:break
	if _ : 
		return "Profense Web Application Firewall (Armorlogic)"