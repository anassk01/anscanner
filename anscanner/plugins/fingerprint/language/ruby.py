#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import findall,I

def ruby(content):
	_ = findall(r'\<a href\=\S*(\.rb|\.rhtml)',content,I)
	if _ != []: return "Ruby"