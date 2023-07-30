import json
from selenium import webdriver
import requests
import re
import random

#requests.post('http://localhost:8000/')
def keyword(message, uid, gid= None):
    if message[0:3] == 'tq': # 天气
        return tianqi(uid, gid, message[3:len(message)])

def tianqi(uid, gid, name):

    url = 'https://www.msn.cn/zh-cn/weather/forecast/in-' + name
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(url)
    driver.save_screenshot('/data/images/result.png')
    if gid != None: # 群聊信息
        requests.get(url='http://127.0.0.1:1981/send_group_msg?group_id={0}&message={1}'.format(gid, r'[CQ:image,file=result.png]'))
        res = requests.get('http://127.0.0.1:11045/')
        return 'OK'

    else: # 私聊信息
        requests.get(url='http://127.0.0.1:1981/send_private_msg?user_id={0}&message={1}'.format(uid, name, r'[CQ:image,file=result.png]'))
        res = requests.get('http://127.0.0.1:11045/')
        return 'OK'