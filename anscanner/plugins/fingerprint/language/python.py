#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import findall,I

def python(content):
	_ = findall(r'\<a href\=\S*(\.py)',content,I)
	if _ != []: return "Python"