
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import time
import shutil
import datetime


nowTime=datetime.datetime.now().strftime('%Y%m%d%H%M%S')#现在

os.mkdir( "D:\\tmp\\desktop\\"+ nowTime);

shutil.move("C:\\Users\\mxl80\\Desktop\\","D:\\tmp\\desktop\\"+nowTime)
 
