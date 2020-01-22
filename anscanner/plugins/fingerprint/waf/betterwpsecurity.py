#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/anassk01/anscanner/blob/master/anscanner/
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt

from re import search,I

def betterwpsecurity(headers,content):
	_ = False
	_ |= search(r'/wp-content/plugins/better-wp-security/',content,I) is not None
	if _:
		return "Better WP Security"