#!/usr/bin/env python
# encoding: utf-8

import requests
from bs4 import BeautifulSoup
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator   #词云库
from PIL import Image
import numpy as np

def searchData(start):
    #设置请求头，
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
               'Host':'movie.douban.com',
               'Accept-Language':'zh-CN,zh;q=0.8',
               'Accept-Encoding':'gzip, deflate, sdch, br',
               'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Cache - Control': 'max - age = 0',
               'Connection': 'keep - alive'

               }
    req = requests.get(
        # https://movie.douban.com/subject/1292052/comments?start=0&limit=20&sort=new_score&status=P
        #url变化规率为start：为页数*20，即每页20条评论
        url='https://movie.douban.com/subject/1292052/comments?start='+str(start)+'&limit=20&sort=new_score&status=P',headers=headers)  # 最基本的GET请求
    if req.status_code == 200:
        html = req.text#网页源码，从响应中获取html源码
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')#解析html源码为BeautifulSoup 对象
        commentList = soup.select('#comments .comment-item p')#获取评论数据，评论数据位置id为comments（div标签）标签下的类名为comment-item的（div标签）标签下的p标签，返回值为列表
        dataString=''#将每页
        for i in commentList :#遍历列表,获取每个p标签的内容，即用户评论
            print(i.string,end='')
            dataString=dataString+i.string#将每条评论拼接一块
        worldCloudCreate(dataString)#调用词云工具，参数：评论数据
    elif req.status_code == 403 :
        print("超过评论页数")
    else :
        print("网络异常")

def worldCloudCreate(dataString):
    image = Image.open(r'.\img\img2.jpg')
    graph = np.array(image)
    #text = open(path.join(d, 'D:\projects\教程目录及说明.txt')).read()#此方式是从本地读取
    #max_font_size为字体显示的最大字号，font_path：字体样式，此样式为微软雅黑，可自行更换样式，background_color：背景颜色，mask：图片遮罩,可以去掉不采用遮罩
    wordcloud = WordCloud(max_font_size=40,font_path= './wryh.ttf',background_color='white',mask=graph).generate(dataString)#设置生成词云，
    # 以下代码以客户客的形式展示词云
    plt.figure("词云图")#指定所绘图名称 ，即弹出框图的标题
    plt.imshow(wordcloud, interpolation="bilinear")# 以图片的形式显示词云
    plt.axis("off")# 关闭图像坐标系
    plt.show()#显示
    # 5、绘制文字的颜色以背景图颜色为参考
    image_color = ImageColorGenerator(graph)  # 从背景图片生成颜色值
    wordcloud.recolor(color_func=image_color)
    #保存为图片
    wordcloud.to_file(r'./test.png')

if __name__ =="__main__":
    start=0#设置第几页，根据自已需要设置页数值
    searchData(start*20)#转换为url中的start值
    pass
