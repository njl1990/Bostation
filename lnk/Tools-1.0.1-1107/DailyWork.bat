@echo off
cd D:\doc\Work\07 日常性事物\06 Daily\Daily log\
echo Daily Log (%date:~3,4%%date:~8,2%%date:~11,2%) >DailyLog-%date:~5,2%%date:~8,2%%date:~11,2%-auto.txt
set path=D:\doc\Work\07 日常性事物\06 Daily\Daily log\DailyLog-%date:~5,2%%date:~8,2%%date:~11,2%-auto.txt
set dp=C:\Users\mxl80\Desktop\Daily-Log.url
echo [InternetShortcut] >>%dp%
echo URL="%path%" >>%dp%
echo IconIndex=20 >>%dp%
echo HotKey=0 >>%dp%
echo IconFile=C:\windows\system32\shell32.dll >>%dp%


