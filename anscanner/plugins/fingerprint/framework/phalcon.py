#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I

def phalcon(headers,content):
	_ = False
	for header in headers:
		_ |= search(r"phalcon-auth-|phalconphp.com|phalcon",header[1])is not None
		if _: break 
	if _: return "Phalcon - PHP Framework"