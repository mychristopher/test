#！/usr/bin/python
# -*- coding: utf-8 -*-

# from datetime import datetime, timedelta, timezone
# tzinfo=timezone.utc
# print(tzinfo)
# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)

# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp
'''

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    # 首先，获取用户输入的时间的datetime
    input_dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')   #str转换为datetime

    # 上面得到的datetime是没有时区的，因此设置用户输入的对应时区
    # 那么此时需要利用正则获取用户输入的时区
    time_zone_num = re.match(r'UTC([+|-][\d]{1,2}):00', tz_str).group(1)    # group(1) 列出第一个括号匹配部分；\d{1,2}表示有一个或者两个数字
    time_zone = timezone(timedelta(hours=int(time_zone_num)))  # 创建时区UTC-？？

    # 将上面得到的datetime强制设置为UTC-？？
    input_dt_tz = input_dt.replace(tzinfo=time_zone)

    return input_dt_tz.timestamp()

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
'''

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
'''
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
'''

from collections import ChainMap
import os, argparse

'''
# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])
'''

'''
# 请写一个能处理去掉=的base64解码函数：
import base64

def safe_base64_decode(s):

    # 判断是否是4的整数u，不够的在末尾添加等号
    if len(s) % 4 != 0:
        s = s + bytes('=', encoding='utf-8') * (4 - len(s) % 4)

    # 解决字符串和bytes类型
    if not isinstance(s, bytes):
        s = bytes(s, encoding='utf-8')

    # 解码
    base64_str = base64.b64decode(s)

    return base64_str


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
'''

'''
# 请编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。

import base64
import struct

def bmp_info(data):
    info = struct.unpack('<ccIIIIIIHH', data[:30])
    # struct.unpack 如果不明白的可以在廖雪峰老师的python课程中仔细看看，通俗理解就是将二进制数据解析出来
    if info[0] == b'B' and (info[1] == b'M' or info[1] == b'A'):
        # 这里是做相应的判断，判断是否为位图
        return {
            'width': info[6],
            'height': info[7],
            'color': info[9]
        }
# 测试
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

bi = bmp_info(bmp_data)
print(bi)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')
'''

'''
# 根据用户输入的口令，计算出存储在数据库中的MD5口令：

import hashlib

def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf8'))
    digest5 = md5.hexdigest()
    return digest5

# 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False

#假如这是保存在数据库的数据，并且口令是用md5计算后的摘要
db = {
    'michael':'e10adc3949ba59abbe56e057f20f883e',
    'bob':'878ef96e86145580c38c87f0410ad153',
    'alice':'99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    if calc_md5(password) == db[user]:
        return True
    else:
        return False

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

#如果你没指定要加密的字符串的字符编码会报错
# TypeError: Unicode-objects must be encoded before hashing
# 输出：
# ok
'''

'''
# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：然后根据修改后的MD5算法实现用户登录的验证

import hashlib, random

db = {}

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48,122)) for i in range(20)])
        #random,randint(48,122)
        #随机生成大于等于48小于等于122的整数
        #chr(random,randint(48,122))
        #生成对应随机数的ascii码对应的字符
        # [chr(random,randint(48,122)) for i in range(20)]
        #列表生成器，其中有20个元素，每个元素字符都是ascii码48到122之间的随机字符
        # ''.join([chr(random.randint(48,122)) for i in range(20)])
        #返回一个以分隔符''连接各个元素后生成的字符串
        self.password = get_md5(password + self.salt)


def register(username, password):
    db[username] = User(username, password)


def login(username, password):
    if username in db:
        user = db[username]
        return user.password == get_md5(password + user.salt)
    else:
        return False

register('michael', '123456')
register('bob', 'abc999')
register('alice', 'alice2008')

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

# 输出：
# ok

#hmac
import hmac, random

db = {}

def hmac_md5(key, s):
    return hmac.new(key.encode('utf8'), s.encode('utf8'), 'md5').hexdigest()
    # return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48,122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)


def register(username, password):
    db[username] = User(username, password)


def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)


register('michael', '123456')
register('bob', 'abc999')
register('alice', 'alice2008')

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

'''

#计算圆周率
'''
# 计算圆周率可以根据公式：利用Python提供的itertools模块，我们来计算这个序列的前N项和：

def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...

    # step 4: 求和:
    return 3.14
'''
'''
import itertools

def pi(n):
    a = 1   # 这是为了后面符号做准备
    s = 0   # 这是为了返回结果做准备
    for i in itertools.count(1):    # 利用itertools.count生成无限序列，从1开始
        if i > 2*n:     # 跳出循环
            return s
        if i % 2 == 1:  # 奇数
            s += (4/i)*a     # 直接求和
            a = -a

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
'''

'''
from urllib import request, parse

# get:

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

# advanced get:

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# post:

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F%3Fjumpfrom%3Dweibocom&jumpfrom=weibocom')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F%3Fjumpfrom%3Dweibocom')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# with proxy and proxy auth:

proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass
'''

'''
# 利用urllib读取JSON，然后将JSON解析为Python对象：

from urllib import request
import json

def fetch_data(url):
    req = request.Request(url)  # 请求url（GET请求）
    with request.urlopen(req) as f:     # 打开url请求（如同打开本地文件一样）
        return json.loads(f.read().decode('utf-8'))  # 读数据 并编码同时利用json.loads将json格式数据转换为python对象

# 测试
URL = 'https://recsidebar.csdn.net/getSideBarRecommend.html'
data = fetch_data(URL)
print(data)
assert data['error'] == True and data['status'] == 400
print('ok')
'''

# from xml.parsers.expat import ParserCreate
#
# class DefaultSaxHandler(object):
#     def start_element(self, name, attrs):
#         print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
#
#     def end_element(self, name):
#         print('sax:end_element: %s' % name)
#
#     def char_data(self, text):
#         print('sax:char_data: %s' % text)
#
# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''
#
# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)



# 请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：
#
# from xml.parsers.expat import ParserCreate
#
# weather_dict = {}  # 定义天气字典
# which_day = 0  # 哪一天
#
#
# # 定义解析类 这三个函数在廖雪峰老师xml这一节中介绍了
# # 包括三个主要函数：start_element(),end_element(),char_data()
# class WeatherSaxHandler(object):
#     def start_element(self, name, attrs):  # 定义start_element函数
#         global weather_dict, which_day
#
#         if name == 'yweather:location':  # 判断并获取XML文档中地理位置信息
#             weather_dict['city'] = attrs['city']  # 将本行XML代码中'city'属性值赋予字典weather_dict中的'city'
#             weather_dict['country'] = attrs['country']  # 执行结束后此时，weather_dict={'city':'Beijing','country'='China'}
#
#         if name == 'yweather:forecast':  # 同理获取天气预测信息
#             which_day += 1  # 第一天天气，获取气温、天气
#             if which_day == 1:
#                 weather_today = {'text': attrs['text'],
#                            'low': int(attrs['low']),
#                            'high': int(attrs['high'])
#                            }
#                 weather_dict['today'] = weather_today  # 此时weather_dict出现二维字典
#             # weather_dict={'city': 'Beijing', 'country': 'China', 'today': {'text': 'Partly Cloudy', 'low': 20, 'high': 33}}
#
#             elif which_day == 2:    # 第二天相关信息
#                 weather_today = {
#                     'text': attrs['text'],
#                     'low': int(attrs['low']),
#                     'high': int(attrs['high'])
#                 }
#                 weather_dict['tomorrow'] = weather_today
#     # weather_dict={'city': 'Beijing', 'country': 'China', 'today': {'text': 'Partly Cloudy', 'low': 20, 'high': 33}, 'tomorrow': {'text': 'Sunny', 'low': 21, 'high': 34}}
#
#     def end_element(self, name):    # end_element函数
#         pass
#
#     def char_data(self, text):   # char_data函数
#         pass
#
# def parse_weather(xml):
#     handler = WeatherSaxHandler()
#     parser = ParserCreate()
#     parser.StartElementHandler = handler.start_element
#     parser.EndElementHandler = handler.end_element
#     parser.CharacterDataHandler = handler.char_data
#     parser.Parse(xml)
#     return weather_dict
#
#
# # XML文档，输出结果的数据来源
# # 将XML文档赋值给data
#
# data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
# <rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
#     <channel>
#         <title>Yahoo! Weather - Beijing, CN</title>
#         <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
#         <yweather:location city="Beijing" region="" country="China"/>
#         <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
#         <yweather:wind chill="28" direction="180" speed="14.48" />
#         <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
#         <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
#         <item>
#             <geo:lat>39.91</geo:lat>
#             <geo:long>116.39</geo:long>
#             <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
#             <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
#             <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
#             <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
#             <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
#             <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
#             <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
#         </item>
#     </channel>
# </rss>
# '''
# # 实例化类
# weather = parse_weather(data)
# # 检查条件是否为True
# assert weather['city'] == 'Beijing', weather['city']
# assert weather['country'] == 'China', weather['country']
# assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
# assert weather['today']['low'] == 20, weather['today']['low']
# assert weather['today']['high'] == 33, weather['today']['high']
# assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
# assert weather['tomorrow']['low'] == 21, weather['tomorrow']['low']
# assert weather['tomorrow']['high'] == 34, weather['tomorrow']['high']
# # 打印到屏幕
# print('Weather:', str(weather))


#解析html
# from html.parser import HTMLParser
# from html.entities import name2codepoint
#
# class MyHTMLParser(HTMLParser):
#
#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)
#
#     def handle_endtag(self, tag):
#         print('</%s>' % tag)
#
#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)
#
#     def handle_data(self, data):
#         print(data)
#
#     def handle_comment(self, data):
#         print('<!--', data, '-->')
#
#     def handle_entityref(self, name):
#         print('&%s;' % name)
#
#     def handle_charref(self, name):
#         print('&#%s;' % name)
#
# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')


# 找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。

from html.parser import HTMLParser
from urllib import request

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._title = [False]
        self._time = [False]
        self._place = [False]
        self.time = ''  # 用于拼接时间

    def _attr(self, attrlist, attrname):
        for attr in attrlist:
            if attr[0] == attrname:
                return attr[1]
        return None

    def handle_starttag(self, tag, attrs):
        if tag == 'h3' and self._attr(attrs, 'class') == 'event-title':
            self._title[0] = True
        if tag == 'time':
            self._time[0] = True
        if tag == 'span' and self._attr(attrs, 'class') == 'event-location':
            self._place[0] = True

    def handle_endtag(self, tag):
       if tag == 'time':
           self._time.append(self.time)  # 将time完整内容放入self._time
           self.time = ''  # 初始化 self.time
           self._time[0] = False

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_data(self, data):
        if self._title[0]:
            self._title.append(data)
            self._title[0] = False
        if self._time[0]:
            self.time += data  # 拼接time
        if self._place[0]:
            self._place.append(data)
            self._place[0] = False

    def handle_comment(self, data):
        pass

    def handle_entityref(self, name):
        if self._time[0]:
            self.time += '-'

    def handle_charref(self, name):
        print('&#%s;' % name)

    def show_content(self):
        for n in range(1, len(self._title)):
            print('Title: %s' % self._title[n])
            print('Time:  %s' % self._time[n])
            print('Place: %s' % self._place[n])
            print('--------------------------------------')

url = "https://www.python.org/events/python-events/"
req = request.Request(url)
with request.urlopen(req) as f:
     html = f.read().decode('utf-8')

parser = MyHTMLParser()
parser.feed(html)
parser.show_content()