#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/anassk01/anscanner/blob/master/anscanner/
# @author:  Thomas Hartmann (thomysec)
# @license: See the file 'LICENSE.txt

from re import search,I

def apachejackrabbit(headers,content):
	_ = False
	_ |= search(r"<\w[^>]*(=\"\/_jcr_content\/){1}[^>]*\>",content) is not None	
	if _ : return "Apache Jackrabbit/Adobe CRX repository"