# -*- coding:utf-8 -*-
#爬虫虎啸网数据进行存储
#时间：2019-1-6
#作者：伟子男
#知识点
#MySQLdb只支持python2.X
import requests
import os
import time
from bs4 import BeautifulSoup
import pymysql 
#2.插入操作
db= pymysql.connect(host="localhost",user="root",
 	password="123456",db="wzn",port=3306,charset="utf8")
 
# 使用cursor()方法获取操作游标
cur = db.cursor()
link = "http://www.santostang.com/"
link1 = "https://www.huxiu.com/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link1, headers= headers)

soup = BeautifulSoup(r.text, "lxml")
# title = soup.find_all(class_ = 'transition msubstr-row2')
# title = soup.find_all(class_='mod-info-flow')
title = soup.find_all('div', class_='mod-thumb pull-left ')
names = [a.a.img for a in title]
for urltitle in names:
	t = urltitle['alt']
	url = urltitle['data-original']
	print('urltitle=%s urL = %s'%(t,url))
	cur.execute("INSERT INTO urls (url, content) VALUES (%s, %s)",(url, t))
cur.close()
db.commit()
db.close()