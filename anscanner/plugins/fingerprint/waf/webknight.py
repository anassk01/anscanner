#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def webknight(headers,content):
	_ = False
	_ |= headers['server'] == 'WebKnight'.lower()
	if _ : 
		return "WebKnight Application Firewall (AQTRONIX)"