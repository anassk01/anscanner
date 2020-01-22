#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from lib.utils.printer import *
from lib.parser.parse import *

def emails(content):
	_list_ = parse(content).getmail()
	if _list_ != None or _list_ != []:
		if len(_list_) >= 2:
			plus('Email address disclosure: %s'%(str(_list_).split('[')[1].split(']')[0]))
		elif len(_list_) == 1:
			plus('Email address disclosure: %s'%_list_[0])