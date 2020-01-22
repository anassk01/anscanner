#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def yunsuo(headers,content):
	_ = False
	_ |= search('<img class=\"yunsuologo\"',content) is not None
	if 'cookie' in headers.keys():
		_ |= search('yunsuo_session',headers['cookie'],I) is not None
	if _ : 
		return "Yunsuo Web Application Firewall (Yunsuo)"