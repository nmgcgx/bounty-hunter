#-*-coding: utf-8 -*- 
import requests
import sys
import datetime
import logging
print('开始推送')
def push_wechat_group(content):
    print('开始推送')
    resp=requests.post("https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=466da795-788d-4334-8a8a-270af7af5031",json={"msgtype":"markdown","markdown":{"content":content}})
    print(resp.json()["errcode"])
    if resp.json()["errcode"] == 0:
        print('push wechat group success',resp.text)

    if resp.json()["errcode"]!= 0:
        raise ValueError("push wechat group failed, %s" % resp.text)

file=sys.argv[1]
with open(file,encoding='utf-8',errors='ignore') as f:
    data = f.read()
push_wechat_group(str(data))