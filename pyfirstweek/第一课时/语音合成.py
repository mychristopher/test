#！/usr/bin/python
# -*- coding: utf-8 -*-
import win32com.client #系统客户端
import time

speak = win32com.client.Dispatch(("SAPI.SPVOICE"))

while 1:
    speak.Speak("sdsada dsadas")
    time.sleep(5)