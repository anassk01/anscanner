#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/anassk01/anscanner/blob/master/anscanner/
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt

from re import findall,I

def php(content):
	_ = findall(r'\<a href\=\S*(\.php|\.php2|\.php3|\.php4|\.php5|\.phtm|\.phtml)',content,I)
	if _ != []: return "PHP"