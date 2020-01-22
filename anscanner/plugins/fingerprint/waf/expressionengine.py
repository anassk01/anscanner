#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/anassk01/anscanner/blob/master/anscanner/
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt

from re import search,I

def expressionengine(headers,content):
	_ = False
	_ |= search(r"Invalid GET Data",content,I) is not None
	if _ : 
		return "ExpressionEngine (EllisLab)"