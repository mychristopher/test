#！/usr/bin/python
# -*- coding: utf-8 -*-
lrcDict = {}
musicLrc = ''''''
musicLrcList = musicLrc.splitlines()
#print(musicLrcList)

for lrcLine in musicLrcList:

    lrcLineList = lrcLine.split("]")
    for index in range(len(lrcLineList) - 1):
        timeStr = lrcLineList[index][1:]

