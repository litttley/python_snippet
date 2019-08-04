#!/usr/bin/env python
# encoding: utf-8

'''
  功能描述:
  @param: $
  @return: $
  @auther: $
  @date: $ $
'''
import tushare as ts
import pandas as pd
import numpy as np
from pandas.core.series import Series

def realtime():
               '''
                  获取实时分笔数据，可以实时取得股票当前报价和成交信息，其中一种场景是，写一个python定时程序来调用本接口（可两三秒执行一次，性能与行情软件基本一致），然后通过DataFrame的矩阵计算实现交易监控，可实时监测交易量和价格的变化。

                  参数说明：

                  symbols：6位数字股票代码，或者指数代码（sh=上证指数 sz=深圳成指 hs300=沪深300指数 sz50=上证50 zxb=中小板 cyb=创业板） 可输入的类型：str、list、set或者pandas的Series对象
                  调用方法：

                  import tushare as ts

                  df = ts.get_realtime_quotes('000581') #Single stock symbol
                  df[['code','name','price','bid','ask','volume','amount','time']]
                  结果显示：

                     code    name     price  bid    ask    volume   amount        time
                  0  000581  威孚高科  31.15  31.14  31.15  8183020  253494991.16  11:30:36
                  返回值说明：

                  0：name，股票名字
                  1：open，今日开盘价
                  2：pre_close，昨日收盘价
                  3：price，当前价格
                  4：high，今日最高价
                  5：low，今日最低价
                  6：bid，竞买价，即“买一”报价
                  7：ask，竞卖价，即“卖一”报价
                  8：volume，成交量 maybe you need do volume/100
                  9：amount，成交金额（元 CNY）
                  10：b1_v，委买一（笔数 bid volume）
                  11：b1_p，委买一（价格 bid price）
                  12：b2_v，“买二”
                  13：b2_p，“买二”
                  14：b3_v，“买三”
                  15：b3_p，“买三”
                  16：b4_v，“买四”
                  17：b4_p，“买四”
                  18：b5_v，“买五”
                  19：b5_p，“买五”
                  20：a1_v，委卖一（笔数 ask volume）
                  21：a1_p，委卖一（价格 ask price）
                  ...
                  30：date，日期；
                  31：time，时间；
                  请求多个股票方法（一次最好不要超过30个）：

                  #symbols from a list
                  ts.get_realtime_quotes(['600848','000980','000981'])
                  #from a Series
                  ts.get_realtime_quotes(df['code'].tail(10))  #一次获取10个股票的实时分笔数据
                  获取实时指数：

                  #上证指数
                  ts.get_realtime_quotes('sh')
                  #上证指数 深圳成指 沪深300指数 上证50 中小板 创业板
                  ts.get_realtime_quotes(['sh','sz','hs300','sz50','zxb','cyb'])
                  #或者混搭
                  ts.get_realtime_quotes(['sh','600848'])
               '''
               initPandas()
               df = ts.get_realtime_quotes('002175')  # Single stock symbol
               # print(df)
               print(df[['code', 'name', 'price', 'low', 'high', 'b1_v', 'b1_p', 'b2_v', 'b2_p', 'b3_v', 'b3_p', 'b4_v', 'b4_p',
                      'b5_v', 'b5_p', 'a1_v', 'a1_p', 'a2_v', 'a2_p', 'a3_v', 'a3_p', 'a4_v', 'a4_p', 'a5_v', 'a5_p', 'volume',
                      'amount', 'time']])
def initPandas():
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 2000)
    pd.set_option('display.max_colwidth', 2000)
    pd.set_option('display.max_rows', None)  # 设置显示最大行

def today_ticks():
    initPandas()
    df = ts.get_today_ticks('002017')
    series = df['type']
    Series()
    print(df)

if __name__ =="__main__":
    today_ticks()