#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys,os,time

#检查主路径是否存在
base_path='c:/lnk/'
if not os.path.exists(base_path):
	os.makedirs(base_path)
	print("create path ...")



print("path...OK")

#检查环境变量

enviroment_path = sys.path

