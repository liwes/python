# -*- coding:utf-8 -*-
#Http get post示例
#时间：2019-1-6
#作者：伟子男
import urllib3
import requests
import json

#Get方法
def getGankData(url):
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
	http = urllib3.PoolManager()
	r = http.request('GET',url,fields={'wd': 'hello'},headers=header)
	print('status = %d data = %s'%(r.status,r.data.decode()))
	# print(r.data.decode())
#POST 上传json数据
def postJsonData(url):
	data={'attribute':'value'}
	encode_data= json.dumps(data).encode()
	http = urllib3.PoolManager()
	r = http.request('POST',
                     url,
                     body=encode_data,
                     headers={'Content-Type':'application/json'}
                 )
	print('postJsonData data = ',r.data.decode('unicode_escape'))
#使用multipart/form-data编码方式上传文件,可以使用和传入Form data数据一样的方法进行,并将文件定义为一个元组的形式(file_name,file_data):
def postFileData(url):	
	with open('1.txt','r+',encoding='UTF-8') as f:
		file_read = f.read()
	http = urllib3.PoolManager()
	r = http.request('POST',
                 url,
                 fields={'filefield':('1.txt', file_read, 'text/plain')
                         })
	print('postFileData data = ',r.data.decode('unicode_escape'))
#上传二进制文件
def postBinaryFileData(url):
	with open('websocket.jpg','rb') as f2:
		binary_read = f2.read()
	http = urllib3.PoolManager()
	r = http.request('POST',
                 'http://httpbin.org/post',
                 body=binary_read,
                 headers={'Content-Type': 'image/jpeg'})
	print('postBinaryFileData data = ',r.data.decode('utf-8'))

def postTest(url):
	header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }
	http = urllib3.PoolManager()
	r = http.request('POST',
                     url,
                     fields={'hello':'world'},
                     headers=header)
	print(r.data.decode())

if __name__ == '__main__':
	# url = 'https://gank.io/api/today'
	hxUrl = 'https://www.huxiu.com/v2_action/article_list'
	postUrl = 'http://httpbin.org/post'
	postJsonData(postUrl)
	# postTest(postUrl)
	# getGankData(hxUrl)