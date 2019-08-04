#!/usr/bin/env python
# encoding: utf-8

# -*- encoding=utf8 -*-
__author__ = "little_y"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import time
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/a248a4c6",
    ])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
poco = AndroidUiautomationPoco()

poco("com.miui.home:id/workspace").offspring("南方航空").offspring("com.miui.home:id/icon_icon").click()

time.sleep(2)

poco("com.csair.mbp:id/include_main_home_view_booking_tv_start").click()
poco(text='广州').click()
poco("com.csair.mbp:id/include_main_home_view_booking_tv_back").click()
poco(text='成都').click()
poco("com.csair.mbp:id/include_main_home_view_booking_llyt_querybtn").click()
array_value=[]
while True:

    time.sleep(3)
    array = poco("android.widget.LinearLayout").offspring("android.view.ViewGroup").\
        offspring("com.csair.mbp:id/frl_place_holder").offspring("com.csair.mbp:id/domestic_list_data_rv")\
        .children()
    num=0
    x_postion=None
    y_postion=None
    try:
        print("array :%s " % len(array))

        for index ,ls2 in enumerate (array):
            child_array = ls2.offspring("android.widget.RelativeLayout").children()
            print("child_array :%s " % len(child_array))
            if len(child_array) <= 10:

                continue

            air_time_start = ls2.offspring("com.csair.mbp:id/item_dep_time_tv").get_text()

            air_start =ls2.offspring("com.csair.mbp:id/item_dep_plane_term_name_tv").get_text()
            air_lishu =ls2.offspring("com.csair.mbp:id/item_fly_time_tv").get_text()
            air_time_end= ls2.offspring("com.csair.mbp:id/item_arr_time_tv").get_text()
            air_end= ls2.offspring("com.csair.mbp:id/item_arr_plane_term_name_tv").get_text()
            price = ls2.offspring("com.csair.mbp:id/item_price_tv").get_text()

            x_postion,y_postion  = ls2.offspring("com.csair.mbp:id/item_price_tv").get_position()

            #ls2.offspring("com.csair.mbp:id/item_price_tv").swipe([y_postion, y_postion], [x_postion * 0.6, y_postion * 0.6])
            print("x:%s,y:%s" % (x_postion,y_postion))
            value = "{air_time_start}#{air_start}#{air_lishu}#{air_time_end}#{air_end}#{price}".format(air_time_start=air_time_start,air_start=air_start,air_lishu=air_lishu,air_time_end=air_time_end,air_end=air_end,price=price)
            if value in array_value:
                continue

            array_value.append(value)
            print("出发时间:%s,出发地点:%s,量程数:%s,到达时间:%s,目的地：%s,价格:%s" % (air_time_start,air_start,air_lishu,air_time_end,air_end,price))

            num=num+1
    except:
       print("异常 ")
    print("num:%s" %num)
    if num == 0:
        keyevent("BACK")
        break
    print("x:%s,y:%s" %(x_postion,y_postion))
    isSwip = poco("android.widget.LinearLayout").offspring("android.view.ViewGroup").offspring("com.csair.mbp:id/frl_place_holder").child("android.widget.RelativeLayout").swipe([0,-y_postion +0.2])
    time.sleep(2)
print("行班数：%s" % len(array_value))
print(array_value)
print("提取完成！")


