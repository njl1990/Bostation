
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import time
import shutil
import datetime


list = ["Foxmail","firefox","FlashHelperService","QQProtect.exe","TeamViewer_Service","Vmware-authd"
        ,"ApplePhotoStreams","TSVNCache","wpscenter","wpscloudsvr","YNoteCefRender","DocToPDF","SogouCloud"
        ,"SogouImeBroker","YoudaoNote","ZhuDongFangYu","TIM","BaiduNetdisk","BaiduNetdiskHost"
        ,"TSVNCache","WeChatWeb","wps","et","DingTalk","QPCore Service"];


for threadname in list:    # 第一个实例
    os.system("taskkill /im "+threadname+".exe /f");
