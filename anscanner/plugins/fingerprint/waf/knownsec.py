#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def knownsec(headers,content):
	_ = False
	_ |= search(r"url\('/ks-waf-error\.png'\)",content) is not None
	if _ : 
		return "KS-WAF (Knownsec)"