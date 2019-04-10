@echo off

set currentpath =D:\Work\07 日常性事物\06 Daily\PDCA\
set dp=C:\Users\mxl80\Desktop\


::设置进入管理范围的文件
set filename1 = 计划进度表-吉利焊装中试线项目.xlsx
set filenamesave1 = D:\Work\00 方案部SVN\项目文件\吉利焊装车间\04 项目管理\02 计划进度\计划进度表-吉利焊装中试线项目-%date:~5,2%%date:~8,2%%date:~11,2%-auto.xlsx



copy %currentpath%\%filename1% %filenamesave1%
del %dp%\%filename1%.url