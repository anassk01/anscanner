#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def secureiis(headers,content):
	_ = False
	_ |= search(r"SecureIIS[^<]+Web Server Protection",content) is not None
	_ |= search(r"http://www.eeye.com/SecureIIS/",content) is not None
	_ |= search(r"\?subject=[^>]*SecureIIS Error",content) is not None
	if _ : 
		return "SecureIIS Web Server Security (BeyondTrust)"