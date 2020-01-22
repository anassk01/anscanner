#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I

def armor(headers,content):
	_ = False
	_ |= search(r'This request has been blocked by website protection from Armor',content,I) is not None
	if _ : 
		return "Armor Protection (Armor Defense)" 