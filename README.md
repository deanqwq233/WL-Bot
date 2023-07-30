# WL-Bot
一个基于Python的QQ群机器人，需要安装依赖flask, requests, selenium

# 方式一：手动下载文件安装

需要go-cqhttp，请下载对应版本并命名为gocq.exe放在程序根目录里。

## 第一次启动，双击START-WL-BOT.exe

在弹出来的窗口中随便输入0~3中一个。

## 关闭窗口后打开config.yml，

在文件开头填写你机器人的QQ号(密码选填)。

在文件末尾将连接服务列表后替换为：

```
servers:
  # HTTP 通信设置
  - http:
      # 是否关闭正向HTTP服务器
      disabled: false
      # 服务端监听地址，用来收QQ信息，可自己设置其它地址
      host: 127.0.0.1
      # 服务端监听端口，用来收QQ信息，可自己设置其它端口
      port: 1981
      # 反向HTTP超时时间, 单位秒
      # 最小值为5，小于5将会忽略本项设置
      # timeout: 5
      middlewares:
        <<: *default # 引用默认中间件
      # 反向HTTP POST地址列表
      post:
        - url: http://127.0.0.1:11045
          secret: ''
```

再次双击START-WL-BOT.exe，启动机器人

# 方式二：一键式安装工具
[带我去Releases](https://github.com/deanqwq233/WL-Bot/releases)

安装完成后在config.yml中填写QQ号(密码可选)

双击START-WL-BOT.exe启动
