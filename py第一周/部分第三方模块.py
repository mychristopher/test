#！/usr/bin/python
# -*- coding: utf-8 -*-

"""
#生成字母验证码图片：
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))	#chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
ttf='C:\Windows/fonts/Arial.ttf'
font = ImageFont.truetype(ttf, 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)    #创建一个可以在给定图像上绘图的对象
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())    #xy为文字的坐标：这个坐标并不是文字的左上角，而是一个与左下角比较接近的位置。
# 模糊:
image = image.filter(ImageFilter.BLUR)  #ImageFilter.BLUR为模糊滤波,处理之后的图像会整体变得模糊。
image.save('code.jpg', 'jpeg')

imagetest = Image.open('E:\progress_python/test/py第一周/code.jpg')
imagetest.show()
"""

# import requests
# r = requests.get('https://www.baidu.com/') # 豆瓣首页
# r.status_code
# r.text

import psutil
p1 = psutil.cpu_count() # CPU逻辑数量   X核非超线程
p2 = psutil.cpu_count(logical=False) # CPU物理核心,X核超线程
print(p1)
print(p2)

p3 = psutil.cpu_times()     #统计CPU的用户／系统／空闲时间
print(p3)

#实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))

# 使用psutil获取物理内存和交换内存信息，分别使用：
p4 = psutil.virtual_memory()
p5 = psutil.swap_memory()
print(p4)
print(p5)

# 可以通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息：

psutil.disk_partitions() # 磁盘分区信息
psutil.disk_usage('/') # 磁盘使用情况
psutil.disk_io_counters() # 磁盘IO

# psutil可以获取网络接口和网络连接信息：
psutil.net_io_counters() # 获取网络读写字节／包的个数
psutil.net_if_addrs() # 获取网络接口信息
psutil.net_if_stats() # 获取网络接口状态
psutil.net_connections()    #获取当前网络连接信息,psutil获取信息也是要走系统接口，而获取网络连接信息需要root权限

# psutil可以获取到所有进程的详细信息：
psutil.pids() # 所有进程ID

p = psutil.Process(3776) # 获取指定进程ID=3776，其实就是当前Python交互环境
p.name() # 进程名称

p.exe() # 进程exe路径

p.cwd() # 进程工作目录

p.cmdline() # 进程启动的命令行

p.ppid() # 父进程ID

p.parent() # 父进程

p.children() # 子进程列表

p.status() # 进程状态

p.username() # 进程用户名

p.create_time() # 进程创建时间

p.terminal() # 进程终端

p.cpu_times() # 进程使用的CPU时间

p.memory_info() # 进程使用的内存

p.open_files() # 进程打开的文件

p.connections() # 进程相关网络连接

p.num_threads() # 进程的线程数量

p.threads() # 所有线程信息

p.environ() # 进程环境变量

p.terminate() # 结束进程

psutil.test()  #模拟出ps命令的效果
