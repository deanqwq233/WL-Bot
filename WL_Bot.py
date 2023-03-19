# coding=utf-8
# -*- coding: UTF-8 -*-
import json
import requests
import re
import random
from selenium import webdriver
def keyword(message, uid, gid = None):
    if message[0:3] == '/天气': # 天气，/天气北京
        return weather(where,message[3:len(message)])
    if message[0:4] == '/版本': # 版本信息，/版本
        return version(message[3:len(message)])


def weather(where):	
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.msn.cn/zh-cn/weather/forecast/in-"+where)
    driver.save_screenshot('weather.png')
    if gid != None: # 如果是群聊信息
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, r'[CQ:image,file=weather.png]'))
def version():
    if gid != None: # 如果是群聊信息
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}版本{2}'.format("WL-Bot V0.01，WL-Bot-一个基于Python和C++的群机器人，https://github.com/deanqwq233/WL-Bot"))