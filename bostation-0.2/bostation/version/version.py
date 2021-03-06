#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys,os,time
import shutil

# 暂时弃用，该功能不需要对子目录的文件进行标准化处理

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

def crt_path(dirname):
	result = []#所有的文件
	pathDir =  os.listdir(dirname)
	for filepath in pathDir:
		apath = os.path.join(dirname, filepath)#合并成一个完整路径
		result.append(apath)
	return result

if __name__=='__main__':
	if len(sys.argv)==1 :
		#	current path 
		pth = '.\\'
	elif len(sys.argv)==2 :
		#	path in argvs
		pth = sys.argv[1]

	print('path:'+pth)

	# get all file in dir
	filelist = crt_path(pth)

	# creat history dir
	hstr_path = os.path.join(pth, "hstr\\")
	print("hstr:"+hstr_path)
	if not os.path.exists(hstr_path):
		os.makedirs(hstr_path) 
	
	
	
	for file in filelist:
		
		# find simbol
		filename=os.path.basename(file)
		
		if 'hstr' in filename:
			continue

		filepath,fullflname = os.path.split(file)
		fname,ext = os.path.splitext(filename)
		# current date
		crtdate=time.strftime("%Y%m%d", time.localtime())
		if '-std.' not in filename:
			# rename
			newname = fname+'-1.0.0-'+str(crtdate)+'-std'+ext
			Newdir=filepath+'\\'+newname
			## print("result:"+Newdir)
			
			# backup old file
			topath=os.path.join(hstr_path,filename)
			print('filename:'+filename)
			shutil.copyfile(file,topath)
			os.rename(file,Newdir)
		else:
			# Version add and Date update
			# Check if Date is today
			segs = fname.split('-')
			seglength=len(segs);

			# Standard file name info 

			stdSeg = segs[seglength-1];
			dateSeg = segs[seglength-2];
			versionSeg = segs[seglength-3];

			# Standard version info 
			versionArray = versionSeg.split('.')
			version3 = versionArray[2]
			version2 = versionArray[1]
			version1 = versionArray[0]

			print('stdSeg:'+stdSeg)
			print('dateSeg:'+dateSeg)
			print('versionSeg:'+versionSeg)
			if crtdate not in dateSeg:
				# find a new version

				#update date
				newfullname=fullflname.replace(dateSeg, crtdate)

				#update version
				version3=str(int(version3)+1)
				newVersion = version1+'.'+version2+"."+version3
				newfullname=newfullname.replace(versionSeg, newVersion)

				newpath = os.path.join(filepath,newfullname)
				print("newpath:"+newpath)
				shutil.copyfile(file,os.path.join(hstr_path,os.path.basename(file)))
				os.rename(file,newpath)
			else:
				print(fname+' is clear');
