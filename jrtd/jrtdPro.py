#!/usr/bin/env python
# encoding: utf-8
from hyper import HTTPConnection
import json
import  sys
import execjs
import  time
import  random
def get_js():
    f = open("./get_as_cp_signature.js", 'r', encoding='gbk',errors='ignore')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr
def initParams(jsstr):

    ctx = execjs.compile(jsstr)

    first_password_Str = ctx.call('get_as_cp_signature', 0)
    first_passwordObj = json.loads(first_password_Str)  # 转json对象可以不用转码

    first_as_Value = first_passwordObj['as']
    first_cp_Value = first_passwordObj['cp']
    first_signature = first_passwordObj['_signature']
    print(first_passwordObj)

    baseUrl = 'https://www.toutiao.com/c/user/article/?page_type=1&user_id=4332276314&max_behot_time=0&count=20&as=%s&cp=%s&_signature=%s' % (  first_as_Value, first_cp_Value, first_signature)
    headers = {
        ":authority": "www.toutiao.com",
        ":method": "GET",
        ':path': "/c/user/article/?page_type=1&user_id=4332276314&max_behot_time=0&count=20&as=%s&cp=%s&_signature=%s" % (first_as_Value, first_cp_Value, first_signature)
        , ":scheme": "https",
        'accept': 'application/json, text/javascript',
        'accept-language': 'zh-CN,zh;q=0.8',
        "content-type": "application/x-www-form-urlencoded",
        'cookie': 'uuid="w:c45107b14a334149bb609512e21ab931"; UM_distinctid=1674b238aaf12d-0b9b07bcbb9ee4-4d045769-1fa400-1674b238ab07ac; __tasessionId=pevrkl2zc1543155857970; CNZZDATA1259612802=697272497-1543148976-%7C1543153769; csrftoken=0125f50415e9058b6c4a8d4287cb4eb5; tt_webid=6627795434445587976',
        # 'accept-encoding': 'gzip,deflate,sdch, br',
        'referer': 'https://www.toutiao.com/c/user/4332276314 /',
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"
      #  ,"x-requested-with":"XMLHttpRequest"
    }
    name = input("是否进入下20抓取(输入exit退出)Y or N:")
    max_behot_time = 'isFirst'
    while True:
        if name == 'Y':  # 表明是第一次使用默认header 及url
            if max_behot_time == 'isFirst':
                max_behot_time = searchDate(headers, baseUrl)
                print("第一次")
            else:
                print('第二次')
                print("max_behot_time:" + str(max_behot_time))
                passwordStr = ctx.call('get_as_cp_signature', str(max_behot_time))
                print(passwordStr)
                passwordObj = json.loads(passwordStr)  # 转json对象可以不用转码
                print("as:%s,cp:%s,_signature:%s" % (passwordObj['as'], passwordObj['cp'], passwordObj['_signature']))
                asValue = passwordObj['as']
                cpValue = passwordObj['cp']
                signature = passwordObj['_signature']
                headers2 = {
                    ":authority": "www.toutiao.com",
                    ":method": "GET",
                    ':path': "/c/user/article/?page_type=1&user_id=4332276314&max_behot_time=%s&count=20&as=%s&cp=%s&_signature=%s" % (  max_behot_time, asValue, cpValue, signature),
                    ":scheme": "https",
                    'cookie': '__tasessionId=7xdpw8ve31543153877912;uuid="w:c45107b14a334149bb609512e21ab931";UM_distinctid=1674b238aaf12d-0b9b07bcbb9ee4-4d045769-1fa400-1674b238ab07ac;CNZZDATA1259612802=697272497-1543148976-%7C1543148976;csrftoken=0125f50415e9058b6c4a8d4287cb4eb5; tt_webid=6627795434445587976',
                    'accept': 'application/json, text/javascript',  # 'accept-encoding': 'gzip,deflate,sdch, br',#加了报错
                    'accept-language': 'zh-CN,zh;q=0.8',
                    'referer': 'https://www.toutiao.com/c/user/4332276314 /',
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0",
                    'content-type': 'application/x-www-form-urlencoded'
                    # , "x-requested-with": "XMLHttpRequest",
                    #  'cookie': 'uuid="w:4746107b99024b83ba7a63326bf1ca01"; UM_distinctid=167483edbc7a71-0a0aa70de306a2-4d045769-1fa400-167483edbc83fc;__tasessionId=1967bauhr1543146215851; csrftoken=ed3eab85ff53f7e1bf71112456ecd8ab;CNZZDATA1259612802=1060750209-1543100376-%7C1543143576; tt_webid=6627586956959696392',
                }
                print(
                    "/c/user/article/?page_type=1&user_id=4332276314&max_behot_time=%s&count=20&as=%s&cp=%s&_signature=%s" % (
                    max_behot_time, asValue, cpValue, signature))
                baseUrl = "https://www.toutiao.com/c/user/article/?page_type=1&user_id=4332276314&max_behot_time=%s&count=20&as=%s&cp=%s&_signature=%s" % (
                max_behot_time, asValue, cpValue, signature)
                max_behot_time = searchDate(headers2, baseUrl)
                print("保存成功!")
        elif name == 'exit':
            sys.exit(0)


def searchDate(headers,url):
    time.sleep(5)
    print("请求url"+url)
    c = HTTPConnection('www.toutiao.com:443')
    first = c.request("GET", url, headers=headers)
    first_response = c.get_response(first)
    text = first_response.read(decode_content=False)
    jsonObject = json.loads(text)  # 转json对象可以不用转码
    array = jsonObject['data']
    print(jsonObject)
    max_behot_time = ""
    try:
        print("下次时间%s"%(jsonObject['next']['max_behot_time']))
        max_behot_time=jsonObject['next']['max_behot_time']
        if max_behot_time == 0 or max_behot_time =="0" :
            raise  BaseException
    except BaseException  :
        print("递归")
        return  searchDate(headers,url)
        print("递归"+url)
    for i in array:
         print("标题：%s,播放量：%s,评论：%s"%(i['title'],i['detail_play_effective_count'],i['comments_count']))
    return max_behot_time


if __name__ =="__main__":
    jsstr = get_js()
    initParams(jsstr)
