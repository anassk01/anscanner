#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I

def expressionengine(headers,content):
	_ = False
	_ |= search(r"Invalid GET Data",content,I) is not None
	if _ : 
		return "ExpressionEngine (EllisLab)"