#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def uspses(headers,content):
	_ = False
	_ |= headers['server'] == 'Secure Entry Server'.lower()
	if _ : 
		return "USP Secure Entry Server (United Security Providers)"