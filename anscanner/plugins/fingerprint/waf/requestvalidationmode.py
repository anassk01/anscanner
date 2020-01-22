#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def requestvalidationmode(headers,content):
	_ = False
	_ |= search(r'ASP.NET has detected data in the request that is potentially dangerous',content) is not None
	_ |= search(r'Request Validation has detected a potentially dangerous client input value',content) is not None	
	if _ : 
		return "ASP.NET RequestValidationMode (Microsoft)"