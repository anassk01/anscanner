#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import findall,I

def php(content):
	_ = findall(r'\<a href\=\S*(\.php|\.php2|\.php3|\.php4|\.php5|\.phtm|\.phtml)',content,I)
	if _ != []: return "PHP"