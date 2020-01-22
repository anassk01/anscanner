#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt'

from urllib2 import HTTPError

class anscanUnboundLocalError(UnboundLocalError):
	pass

class anscanDataException(Exception):
	pass

class anscanNoneException(Exception):
	pass

class anscanInputException(Exception):
	pass

class anscanGenericException(Exception):
	pass

class anscanConnectionException(HTTPError):
	pass

class anscanKeyboardInterrupt(KeyboardInterrupt):
	pass