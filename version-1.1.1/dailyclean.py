#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys,os,time
import shutil,datetime


def all_path(dirname):

	result = []#所有的文件
	for maindir, subdir, file_name_list in os.walk(dirname):
		#print("1:",maindir) #当前主目录
		#print("2:",subdir) #当前主目录下的所有目录
		#print("3:",file_name_list)  #当前主目录下的所有文件
		for filename in file_name_list:
			apath = os.path.join(maindir, filename)#合并成一个完整路径
		#	print(apath)
			result.append(apath)
	return result


if __name__=='__main__':
	
	# get all file in dir
	filelist = all_path("C:\\Users\\htyw\\Desktop")

	year = datetime.datetime.now().year
	month = datetime.datetime.now().month
	day = datetime.datetime.now().day

	daily_path ="D:\\dailylog\\"+str(year)+"\\"+str(month)+"\\"+str(day)

	if not os.path.exists(daily_path):
		os.makedirs(daily_path) 

	for file in filelist:
		filename=os.path.basename(file)
		if '.lnk' in filename:
			continue
		if '~$' in filename:
			continue
		if '.ini' in filename:
			continue
		try:
			#copy:
			topath = os.path.join(daily_path, filename)
			shutil.copyfile(file,topath)
			os.remove(file)
		except IOError:
			print(IOError)
		print(file)