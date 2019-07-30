#!/usr/bin/env python
# encoding: utf-8
import requests
from  hyper import HTTPConnection
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import json
import time
from lxml import etree
import  re
from selenium import webdriver
import random
from fake_useragent import UserAgent



import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def getSignature(uid):
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    option.add_argument('UTF-8')
    driver = webdriver.Chrome(chrome_options=option)
    driver.get("file:///D:/%E6%A1%8C%E9%9D%A22/soJson/images/douyin_signature-master/demo.html")
    driver.execute_script("mybutton(" +uid+ ")")
    element = driver.find_element_by_id('signc')
    return element.text
def getUid(url):
    headers = {
        "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        "accept-language": 'zh-CN,zh;q=0.8',
       # "Host": "www.iesdouyin.com",
        "Host": "v.douyin.com",

        "Cookie":'tt_webid=6580632312453727748'
    }
    urlLocation=''
    req = requests.get(url,headers=headers,verify=False)

    for his in req.history:#获取重定向url
        urlLocation= his.headers['Location']
        break

   # urlLocation =req.headers['Location']
    print(urlLocation)
    head2Path='/share'+urlLocation.split('com/share')[1]
    headers2 = {
        ":authority": "www.iesdouyin.com",
        ":method": "GET",
        # ':path': '/aweme/v1/aweme/post/?user_id=71220238852&count=21&max_cursor=0&aid=1128&_signature=4pkvXxARudWZoEyZjBt8q-KZL0&dytk=32258caa1ace4e923e0375002da84f68'
      #  ':path': '/share/video/6580331002172804359/?region=CN&mid=6576435383842638595&titleType=title&utm_source=copy_link&utm_campaign=client_share&utm_medium=android&app=aweme&iid=38562272372&timestamp=1532191502'
        ':path':  head2Path
        , ":scheme": "https",
        "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        "accept-language": 'zh-CN,zh;q=0.8',
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"

    }
    c = HTTPConnection('www.iesdouyin.com:443')
    #url = 'https://www.amemv.com/aweme/v1/aweme/post/?user_id=%s&count=21&max_cursor=%s&aid=1128&_signature=4pkvXxARudWZoEyZjBt8q-KZL0&dytk=32258caa1ace4e923e0375002da84f68' % (
    #userid, maxcursor)
    first = c.request("GET", url=urlLocation, headers=headers2)
    first_response = c.get_response(first)

    print(first_response.reason)
    html=first_response.read(decode_content=False).decode('utf-8')
    p1='<div class="user-info">.*?</div>'
    p2='<p class="user-info-name">(.*?)</p>'
    p3='<p class="user-info-id">(.*?)<i class="icon iconfont ">'
    p4='<i class="icon iconfont "> (.*?) </i>'
    p5='uid: "(.*?)",'
    pattern1 = re.compile(p5)  # 我们在编译这段正则表达式

    matcher1 = re.search(pattern1, html)  # 在源文本中搜索符合正则表达式的部分
    return matcher1.group(1)
def getUserInfo(signature,dutk,userid,maxcursor,nickname):

    while True:

            headers = {
                ":authority": "www.amemv.com",
                ":method": "GET",
               # ':path': '/aweme/v1/aweme/post/?user_id=71220238852&count=21&max_cursor=0&aid=1128&_signature=4pkvXxARudWZoEyZjBt8q-KZL0&dytk=32258caa1ace4e923e0375002da84f68'
                ':path': '/aweme/v1/aweme/post/?user_id=%s&count=21&max_cursor=%s&aid=1128&_signature=%s&dytk=%s' %(userid,maxcursor,signature,dutk)
                , ":scheme": "https",
                "accept":'application/json',
                #"accept-encoding":'gzip, deflate, sdch, br',#加上此头报错UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte
               #原因 "Accept-Encoding": "gzip, deflate",
              # 这条信息代表本地可以接收压缩格式的数据，而服务器在处理时就将大文件压缩再发回客户端，IE在接收完成后在本地对这个文件又进行了解压操作。出错的原因是因为你的程序没有解压这个文件，所以删掉这行就不会出现问题了
                "accept-language":'zh-CN,zh;q=0.8',
                "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
                ,"referer":'https://www.amemv.com/share/user/%s' % userid,
                'Cookie':'_ga=GA1.2.1994146776.1532173543; _gid=GA1.2.380526035.1532528828'

            }
            c = HTTPConnection('www.amemv.com:443')
            url='https://www.amemv.com/aweme/v1/aweme/post/?user_id=%s&count=21&max_cursor=%s&aid=1128&_signature=%s&dytk=%s' %(userid,maxcursor,signature,dutk)
            print(url)
            first  =c.request("GET",url=url,headers=headers)
            first_response = c.get_response(first)
           # print(first_response.headers)
            if first_response.status == 200:
                text = first_response.read(decode_content=False)
                print(text)
                jsonObject = json.loads(text)  # 转json对象可以不用转码
                awemeList =jsonObject['aweme_list']
                if len(awemeList) > 0:
                        hasMore = jsonObject['has_more']
                        for ls in awemeList:
                            urlVideo =ls['video']['play_addr']['url_list'][0]
                            shareDes= ls['share_info']['share_desc']
                            #print(urlVideo)
                            print(shareDes)
                            getVideos(urlVideo,shareDes,nickname)
                        maxcursor = jsonObject['max_cursor']
                        time.sleep(3)
                        if hasMore == 0:
                            break

                else:
                    break


def getVideos(url,shareDes,nickname):
    ua = UserAgent(path="D:\\pythonProject\douYin2\\0.1.json")
    print("ua:"+ua.random)
    headers = {}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
     #   "User-Agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Host': 'aweme.snssdk.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': ua.random

    }

    urlLocation = ''
    print("vide0:"+url)
    try:

         req = requests.get(url=url, headers=headers, verify=False)
         for his in req.history:  # 获取重定向url
             urlLocation = his.headers['Location']
             break

    except requests.exceptions.ConnectionError :
        print('ConnectionError -- please wait 3 seconds')
        time.sleep(3)
        getVideos(url,shareDes,nickname)#递归调多加载几次就可以加载回业
        return None


    try:

        head2Host = urlLocation.split('com/')[0]
       # print(head2Host)
        head2Host = head2Host.split("http://")[1]
        head2Host = head2Host + "com"
   # print(urlLocation)
    #print(head2Host)

        headers2 = {
            'Accept': '*/*',
            'Accept-Encoding': 'identity;q=1, *;q=0',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            "User-Agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            'Host': head2Host,
            "Connection": "keep-alive",
            'Host': head2Host,
            'referer': urlLocation,
            'Range': 'bytes=0-'

        }
        print("urlLocationvedio"+urlLocation)
        req2 = requests.get(url=urlLocation, headers=headers2, verify=False)
        contents = req2.content
        #print(contents)

        #print(req.headers)
        filename = "test06\\"+nickname+"_"+shareDes+ "0.mp4"
        print(filename)
        with open(filename, "wb") as f:
            f.write(contents)

        time.sleep(5)
    except IndexError:
        print("urllocation:"+urlLocation)
    except :
        print("未知错误")

def getDytk(uid):
    headers = {
        ":authority": "www.amemv.com",
        ":method": "GET",
        # ':path': '/aweme/v1/aweme/post/?user_id=71220238852&count=21&max_cursor=0&aid=1128&_signature=4pkvXxARudWZoEyZjBt8q-KZL0&dytk=32258caa1ace4e923e0375002da84f68'
        ':path': '/share/user/%s' % uid
        , ":scheme": "https",
        "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        # "accept-encoding":'gzip, deflate, sdch, br',#加上此头报错UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte
        # 原因 "Accept-Encoding": "gzip, deflate",
        # 这条信息代表本地可以接收压缩格式的数据，而服务器在处理时就将大文件压缩再发回客户端，IE在接收完成后在本地对这个文件又进行了解压操作。出错的原因是因为你的程序没有解压这个文件，所以删掉这行就不会出现问题了
        "accept-language": 'zh-CN,zh;q=0.8',
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
    }
    url='https://www.amemv.com/share/user/%s' % uid
    c = HTTPConnection('www.iesdouyin.com:443')
    # url = 'https://www.amemv.com/aweme/v1/aweme/post/?user_id=%s&count=21&max_cursor=%s&aid=1128&_signature=4pkvXxARudWZoEyZjBt8q-KZL0&dytk=32258caa1ace4e923e0375002da84f68' % (
    # userid, maxcursor)
    first = c.request("GET", url=url, headers=headers)
    first_response = c.get_response(first)

    print(first_response.headers)
    # print(first_response.status)
    html = first_response.read(decode_content=False).decode('utf-8')

    p1 = "dytk: '(.*?)'"
    p2 = '<p class="nickname">(.*?)</p>'
    pattern1 = re.compile(p1)  # 我们在编译这段正则表达式
    pattern2 = re.compile(p2)  # 我们在编译这段正则表达式
    matcher1 = re.search(pattern1, html)  # 在源文本中搜索符合正则表达式的部分
    matcher2 = re.search(pattern2, html)

    return  matcher1.group(1),matcher2.group(1)


def test():
    url = 'https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f840000bf5be7g858lot4a592c0&line=0'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        "User-Agent":'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1' ,
        'Host': 'aweme.snssdk.com',

    }

    urlLocation=''
    req = requests.get(url=url, headers=headers, verify=False)
    for his in req.history:  # 获取重定向url
        urlLocation = his.headers['Location']
        break

    head2Host =   urlLocation.split('com/')[0]
    print(head2Host)
    head2Host = head2Host.split("http://")[1]
    head2Host=head2Host+"com"
    print(urlLocation)
    print(head2Host)

    headers2 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        "User-Agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Host': head2Host,
        'referer':urlLocation

    }
    req2 = requests.get(url=urlLocation, headers=headers2, verify=False)
    contents= req2.content
    print(contents)
  

    # print(req.headers)
    filename =  "2.mp4"
    print(filename)
    with open(filename, "wb") as f:
        f.write(contents)
        time.sleep(5)

def test03():
    url = 'https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f840000bf676t6t8aheufn87830&amp'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        "User-Agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Host': 'aweme.snssdk.com',

    }

    req = requests.get(url=url, headers=headers, verify=False)

    print(req.content)

    # print(req.headers)
    filename = "xx.mp4"
    print(filename)
    with open(filename, "wb") as f:
        f.write(req.content)
        time.sleep(5)

if __name__ =='__main__':


   #uid =  getUid('http://v.douyin.com/eYY1sa/')#通过分享键接获取uid


     #  uid =  getUid('http://v.douyin.com/RFCxFa/')#通过分享键接获取uid
       #uid =  getUid('http://v.douyin.com/RFWTbE/')#通过分享键接获取uid
       uid =  getUid('http://v.douyin.com/6tVEYv/')#通过分享键接获取uid
       print("uid:%s" % uid)
       signature = getSignature(uid)#获取加密signature
       print("signature:%s" % signature)
       dytk,nickname= getDytk(uid)
       print("dytk:%s,nickname:%s" % (dytk,nickname))
       getUserInfo(signature,dytk,uid,"0",nickname)

   # test03()
