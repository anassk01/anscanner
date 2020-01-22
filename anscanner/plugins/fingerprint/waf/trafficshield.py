#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I 

def trafficshield(headers,content):
	_ = False
	_ |= headers['server'] == "F5-TrafficShield".lower()
	_ |= search(r'st8\(id|_wat|_wlf\)',str(headers.values()),I) is not None
	if _ : 
		return "TrafficShield (F5 Networks)"