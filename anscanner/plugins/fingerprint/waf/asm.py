#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/anassk01/anscanner/blob/master/anscanner/
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt

from re import search,I

def asm(headers,content):
	_ = False
	_ |= search(r'The requested URL was rejected. Please consult with your administrator.',content,I) is not None
	if _ : 
		return "Application Security Manager (F5 Networks)" 