#!/usr/bin/env python
# encoding: utf-8
from selenium import webdriver

from selenium import webdriver
#driver = webdriver.PhantomJS(executable_path=r'./phantomjs.exe')
option = webdriver.ChromeOptions()
option.add_argument("headless")
option.add_argument('UTF-8')
driver = webdriver.Chrome(chrome_options=option)

driver.get("file:///C:/Users/little_y/Desktop/soJson/images/douyin_signature-master/demo.html")
driver.execute_script("mybutton("+str(95026013333)+")")
element = driver.find_element_by_id('signc')
print(element.text)
