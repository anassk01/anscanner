#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def sophos(headers,content):
	_ = False
	_ |= search(r"Powered by UTM Web Protection",content) is not None
	if _ : 
		return "UTM Web Protection (Sophos)"