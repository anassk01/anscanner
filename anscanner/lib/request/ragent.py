#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    anscan - Web Application Scanner
# @repo:    https://github.com/--/anscan
# @author:  anassk (--)
# @license: See the file 'LICENSE.txt

from os import path
from random import randint
from lib.utils.readfile import *

def ragent():
	"""random agent"""
	user_agents = ()
	realpath = path.join(path.realpath(__file__).split('lib')[0],'lib/db/')
	realpath += "useragent.anscan"
	for _ in readfile(realpath):
		user_agents += (_,)
	return user_agents[randint(0,len(user_agents)-1)]