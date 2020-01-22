#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def sitelock(headers,content):
	_ = False
	_ |= search(r"SiteLock Incident ID",content) is not None
	if _ : 
		return "TrueShield Web Application Firewall (SiteLock)"