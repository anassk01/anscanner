#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/anassk01/anscanner/blob/master/anscanner/
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt

from re import findall,I

def java(content):
	_ = findall(r'\<a href\=\S*(\.do|\.jhtml|\.jsp|\.jspa|\.jspx|\.jws|\.wss|\.action)',content,I)
	if _ != []: return "Java"