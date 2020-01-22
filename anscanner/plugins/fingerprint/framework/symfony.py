#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from re import search,I

def symfony(headers,content):
	_ = False
	_ |= search(r"\"powered by symfony\"",content) is not None
	_ |= search(r"Powered by \<a \href\=\"http://www.symfony-project.org/\"\>",content) is not None
	if _ : return "Symfony - PHP Framework"