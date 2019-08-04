#!/usr/bin/env python
# encoding: utf-8

import  tushare as ts
import pandas as pd
from datetime import datetime

'''
 功能描述: 
     参数: 
     参数: code : 股票代码
   返回值: 
'''
def getdaily(pro,code,startDate,endDate):
    szcode=code+".SZ"
    df = pro.query('daily', ts_code=szcode, start_date=startDate, end_date=endDate)
    if len(df.values) == 0:
        shcode=code+".SH"
        df = pro.query('daily', ts_code=shcode, start_date=startDate, end_date=endDate)

    print(df.sort_values(by=['trade_date']))
   # print(df.loc[:,'open'].max())
    #print(df.loc[:, 'open'].min())

    name,price = stock_symbol(code)
    print("\n")
    print(df.loc[:,'open'].mean())
    print("开盘价最大值:%s ; 开盘价最小值:%s ;均值:%s\n "  % (df.loc[:,'open'].max(), df.loc[:, 'open'].min(),df.loc[:,'open'].mean()))
    print("收盘价最大值:%s ; 收盘价最小值:%s;均值:%s\n" % (df.loc[:, 'close'].max(), df.loc[:, 'close'].min(),df.loc[:,'close'].mean()))
    print("名称：%s;股票代码：%s;上市价格:%s" %(name , code , price ))

'''
  功能描述:设置打印行数及宽度 
      参数: 无
    返回值: 无
'''
def initPandas():
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_colwidth', 1000)
    pd.set_option('display.max_rows', None)  # 设置显示最大行


'''
  功能描述:获取股票信息
      参数: code: 股票代码
    返回值: name 股票名称， price : 股票代码
'''
def stock_symbol(code):
    df = ts.get_realtime_quotes(code.split(".")[0])  # Single stock symbol
    return  df['name'][0] ,df['price'][0]
'''
  功能描述: 导出excel数据
      参数: 无
    返回值: 无
'''

def exportExcel(df):
    writer = pd.ExcelWriter('d:\output.xlsx')
    # 生成excel文档，默认支持DataFrame数据类型
    df.to_excel(writer, 'Sheet1', index=False)
    writer.save()
    # print(df)

if __name__ == '__main__':
    pro = ts.pro_api('8f227fb902c3791148955bc007be806af3ba28ffdb3563baf6ef2fd4')
    initPandas()
    #code='601890'#亚星锚链
    #code='002024'#苏宁易购
    #code='002181'#粤 传 媒
    #code='600029'#南方航空
    while True:
        code = input("请输入股票代码：")
        if code !="n":
            #code='000735'#南方航空
            startDate='20170201'#
            #endDate='20190313'
            dt = datetime.now()
            endDate=dt.strftime("%Y%m%d")
            #print(dt.strftime("%Y%m%d"))
            getdaily(pro,code,startDate,endDate)
            #stock_symbol()
        else:
            break