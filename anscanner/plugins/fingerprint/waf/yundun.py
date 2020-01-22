#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def yundun(headers,content):
	_ = False
	_ |= headers['server'] == 'YUNDUN'
	if 'x-cache' in headers.keys():
		_ |= headers['x-cache'] == 'YUNDUN'
	if _ : 
		return "Yundun Web Application Firewall (Yundun)"