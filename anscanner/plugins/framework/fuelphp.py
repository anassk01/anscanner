#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/anassk01/anscanner/blob/master/anscanner/
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt

from re import search,I

def fuelphp(headers,content):
	_ = False
	for header in headers.items():
		_ |= search("fuelcid=",header[1]) is not None
		if _ : break
	_ |= search(r"Powered by \<a href\=\"http://fuelphp.com\"\>FuelPHP\<\/a\>",content) is not None 
	if _ : return "FuelPHP - PHP Framework"