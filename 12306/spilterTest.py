#!/usr/bin/python3
#-*- coding:utf-8 -*-

from splinter import Browser
from html.parser import HTMLParser
from pyvirtualdisplay import Display #配置无界面chrome用

import  time
def getFunc():
    #http://blog.csdn.net/windanchaos/article/details/54898354
    #火车票账号：xxxxxxxxxxxxx
    #密码：ZLfdHcp9559
    browser = Browser("chrome")
    #url = "https://kyfw.12306.cn/otn/leftTicket/init"
    url = "https://kyfw.12306.cn/otn/login/init"

    b = Browser(driver_name="chrome")
    b.visit(url)
    b.find_by_text(u"登录").click()
    #b.fill("loginUserDTO.user_name","xxxxxxxxxxxxx")
    #b.fill("userDTO.password","ZLfdHcp9559")
    b.fill("loginUserDTO.user_name","1301935424@qq.com")
    b.fill("userDTO.password","Fai13585654195")
    daihao=""
    daihao2=""
    startDate=""
    isValue=True
    while isValue:
        daihao=input("请输入出发城市代号例(广州GZQ):")
        daihao2=input("请输入到站城市代号例(济宁JIK):")
        startDate=input("请输入出发日期例例(2018-02-16):")
        if daihao!="" and daihao2!="" and startDate!="":
            isValue=False
    isTrue=True
    count=0
    while isTrue:
        try:

             sec_found = b.find_by_id('selectYuding').click()

             b.execute_script("$('#fromStation').val('"+daihao+"')")
             b.execute_script("$('#toStation').val('"+daihao2+"')")
             b.execute_script("$('#train_date').removeAttr('readonly')")
             b.execute_script("$('#train_date').val('"+startDate+"')")
            # third_found = b.find_by_text(u'查询').click()
             b.execute_script("$('#query_ticket').removeClass('btn-disabled')")
             b.execute_script("$('#query_ticket').click()")
             b.find_by_text(u'T-特快')[0].click()
             cc=b.find_by_xpath('//a[@class="btn72"]')
             if len(cc)==0:
                print("正在进行{0}次抢票中.....".format(count))
                count=count+1
                time.sleep(3)
                continue
             else:
                b.find_by_text(u'预订')[0].click()
                time.sleep(5)
                isTrue=False
        except :

            print("正在努力查询......")


#b.execute_script("$('#seatType_1').click()")
#硬座为1软座为2硬卧为3软卧为4
    #isTrue2=True
    #while isTrue2:
        #try:
    isTrue2=True
    isTrue3=True
    if True:
            while isTrue2:
                try:
                     b.find_by_text(u'张鲁峰')[1].click()
                    #b.find_by_text(u'刘明豪')[0].click()
                     b.execute_script("$('#seatType_1 option[value=\"1\"]').attr('selected',true)")
                     b.find_by_text(u"提交订单")[0].click()
                     isTrue2=False
                except:
                     print("正在加载订单页面")

            while isTrue3:
                try:
                    ds=b.find_by_xpath('//div[@class="dhtmlx_window_active"]')
                    print("刷新确定页面")
                    if len(ds)!=0:
                        ss=b.execute_script("document.getElementById('qr_submit_id').click()")
                        print("确认即将进入支付页面")
                        isTrue3=False
                except:
                    print("正加加载身分")
    input("请到支付页面支付")

    b.quit()

if __name__=="__main__":
    input("按任意键开始")
    getFunc()