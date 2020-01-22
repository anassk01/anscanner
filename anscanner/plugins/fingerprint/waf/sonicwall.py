#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def sonicwall(headers,content):
	_ = False
	_ |= search(r"This request is blocked by the SonicWALL",content) is not None
	_ |= search(r"Web Site Blocked.+\bnsa_banner",content) is not None
	_ |= headers['server'] == 'sonicwall'
	if _ : 
		return "SonicWALL (Dell)"