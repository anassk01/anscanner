#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def wallarm(headers,content):
	_ = False
	_ |= headers['server'] == 'nginx-wallarm'
	if _ : 
		return "Wallarm Web Application Firewall (Wallarm)" 