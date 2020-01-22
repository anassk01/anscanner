#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/anassk01/anscanner/blob/master/anscanner/
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt

from re import search,I

def ciscoacexml(headers,content):
	_ = False
	for header in headers.items():
		_ |= search(r'ace xml gateway',header[1],I) is not None
		if _: break
	if _ : 
		return "Cisco ACE XML Gateway (Cisco Systems)"