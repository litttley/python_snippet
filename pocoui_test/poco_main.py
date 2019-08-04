#!/usr/bin/env python
# encoding: utf-8
# -*- encoding=utf8 -*-# -*- encoding=utf8 -*-
__author__ = "little_y"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/a248a4c6",
    ])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import time
poco = AndroidUiautomationPoco()

poco("com.miui.home:id/workspace").offspring("抖音短视频").offspring("com.miui.home:id/icon_icon").click()
time.sleep(3)

def save_error_log(path,content):
    dir = path.split("/")[1]
    if os.path.exists(dir):
        pass
    else:
        os.makedirs(dir)
    with open(path, 'a+',encoding='utf-8') as f:
        f.write(content)
        f.write("\n")

while True :
    try:
        title = poco("android:id/content").child("android.widget.FrameLayout").child("com.ss.android.ugc.aweme:id/dsq").child("com.ss.android.ugc.aweme:id/afq").offspring("com.ss.android.ugc.aweme:id/bl2").offspring("com.ss.android.ugc.aweme:id/af4").offspring("com.ss.android.ugc.aweme:id/bjl").offspring("com.ss.android.ugc.aweme:id/dr6").offspring("com.ss.android.ugc.aweme:id/a3q").get_text()
        dian_zan= poco("android:id/content").child("android.widget.FrameLayout").child("com.ss.android.ugc.aweme:id/dsq").child("com.ss.android.ugc.aweme:id/afq").offspring("com.ss.android.ugc.aweme:id/bl2").offspring("com.ss.android.ugc.aweme:id/af4").offspring("com.ss.android.ugc.aweme:id/bjl").offspring("com.ss.android.ugc.aweme:id/a52").get_text()

        ping_lin = poco("android:id/content").child("android.widget.FrameLayout").child("com.ss.android.ugc.aweme:id/dsq").child("com.ss.android.ugc.aweme:id/afq").offspring("com.ss.android.ugc.aweme:id/bl2").offspring("com.ss.android.ugc.aweme:id/af4").offspring("com.ss.android.ugc.aweme:id/bjl").offspring("com.ss.android.ugc.aweme:id/uw").get_text()
        print("标题:%s,点赞:%s,评论：%s"%(title,dian_zan,ping_lin))
        save_error_log("D:/douyin.txt",title)
    except Exception as e :
        continue
    poco("com.ss.android.ugc.aweme:id/ali").swipe([-0.0833, -0.8])
    time.sleep(4)







