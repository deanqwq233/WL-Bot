from flask import Flask, request
import requests

import api

app = Flask(__name__)

@app.route('/', methods=["POST"])
def post_data():
    if request.get_json().get('message_type') == 'private':  # 是私聊信息
        uid = request.get_json().get('sender').get('user_id')  # 获取信息发送者的QQ号
        message = request.get_json().get('raw_message')  # 获取原始信息
        api.keyword(message, uid)  # 传到后台

    if request.get_json().get('message_type') == 'group':  # 是群聊信息
        gid = request.get_json().get('group_id')  # 获取群号
        uid = request.get_json().get('sender').get('user_id')  # 获取信息发送者的QQ号
        message = request.get_json().get('raw_message')  # 获取原始信息
        api.keyword(message, uid, gid)  # 传到后台
    return 'OK'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=11045)