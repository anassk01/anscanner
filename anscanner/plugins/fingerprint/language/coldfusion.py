#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/anassk01/anscanner/blob/master/anscanner/
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt

from re import findall,I

def coldfusion(content):
	_ = findall(r'\<a href\=\S*(\.cfm|\.cfml)',content,I)
	if _ != []: return "ColdFusion"