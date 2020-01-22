#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import findall,I

def asp(content):
	_ = findall(r'\<a href\=\S*(\.asp)',content,I)
	if _ != []: return "ASP"