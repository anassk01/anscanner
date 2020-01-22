#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt'

def readfile(path):
	""" read file """
	if path != None or path != "":
		return [line.strip() for line in open(path,'rb')]
	return