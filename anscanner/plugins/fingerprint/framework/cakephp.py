#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I

def cakephp(headers,content):
	_ = False
	for header in headers.items():
		_ |= search("CAKEPHP=",header[1]) is not None
		if _ : break
	if _ : return "CakePHP - PHP Framework"