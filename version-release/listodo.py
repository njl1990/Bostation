#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys,os,time

if __name__=='__main__':
	
	if len(sys.argv)==1 :
		#	current path 
		pth = '.\\'
	elif len(sys.argv)==2 :
		#	path in argvs
		pth = sys.argv[1]

	print('path:'+pth)