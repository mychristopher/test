#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
async web application.
'''

import logging
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web


logging.basicConfig(level=logging.INFO)

# 主要思路：
# 　　理解 asyncio、aiohttp 基本应用
# 　　使用 asyncio 异步 IO 模块创建服务协程，监听相应端口
# 　　使用 aiohttp 异步 Web 开发框架，处理 HTTP 请求，构建并返回 HTTP 响应
def index(request):
    """响应函数"""
    return web.Response(body=b'<h1>Awesome</h1>',headers={'content-type':'text/html'})

async def init(loop):
    """Web App服务器初始化"""
    # 制作响应合集
    app = web.Application(loop=loop)
    # 把响应函数添加到响应函数集合
    app.router.add_route(method='GET', path='/', handler=index)
    # 创建服务器（连接网址、端口，绑定handler）
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

# 创建事件
loop = asyncio.get_event_loop()
# 运行
loop.run_until_complete(init(loop))
# 服务器不关闭
loop.run_forever()