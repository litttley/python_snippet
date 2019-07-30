#!/usr/bin/env python
# encoding: utf-8
#!/usr/bin/env python
# encoding: utf-8

import requests
from bs4 import BeautifulSoup
from os import path
import json
import sys
import time

def searchData(start,num):
    #设置请求头，
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
               'Host':'movie.douban.com',
               'Accept-Language':'zh-CN,zh;q=0.8',
               'Accept-Encoding':'gzip, deflate, sdch, br',
               'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Cache - Control': 'max - age = 0',
               'Connection': 'keep - alive',
              # 'Content-Type': 'application/json; charset=UTF-8',
               }
    try:
        # url变化规率为start：为页数*20，即每页20条评论
        req = requests.get(url='https://movie.douban.com/subject/1867345/comments?start='+str(start)+'&limit=20&sort=new_score&status=P&comments_only=1',headers=headers)  # 最基本的GET请求
        if req.status_code == 200:
            jsonStr = req.text#网页源码，从响应中获取html源码
            jsonObject = json.loads(jsonStr)
            xmlStr =jsonObject['html']
            soup = BeautifulSoup(xmlStr, 'lxml')#解析html源码为BeautifulSoup 对象
            pflags = soup.findAll('p',{'class':""})#获取评论数据，评论数据位置id为comments（div标签）标签下的类名为comment-item的（div标签）标签下的p标签，返回值为列表
            dataString=''#将每页
            str2=''
            #print(pflags)

            for i in pflags :#遍历列表,获取每个p标签的内容，即用户评论
                #print(i.string,end='')
                if (i.string != '') and (i.string is not None):
                    sqlStr= i.string.strip().replace("\n", "")
                    str2=str2+"INSERT INTO comment VALUES('{0}', '{1}');\n".format(num,sqlStr)
                    num=num+1
            saveSQL(str2,start)
            time.sleep(2)
        elif req.status_code == 403 :
            print("超过评论页数")
        else :
            print("网络异常")
    except exceptions.Timeout as e:
          pass
    except exceptions.HTTPError as e:
       pass
    return num

def saveSQL(str,start):
    with open("./comment.sql", encoding="utf-8", mode="a") as data:
        data.write(str)
    print("评论(第%s页):\n%s已成功写入#" % (num, str))

if __name__ =="__main__":
    start=1
    name = input("是否爬取Y(Y:是，N：重新输入，输入exit退出):")
    num=1
    while True:
        if name == "Y":

            num=searchData(start * 20,num)  # 转换为url中的start值
            start=start+1
            name='Y'
            print("正在加爬取网页数据#####")
            time.sleep(2)
        elif name == 'exit':
            sys.exit(0)
        else:
            name = input("是否爬取Y(Y:是，N：重新输入，输入exit退出):")

