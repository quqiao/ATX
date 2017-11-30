# coding=utf-8

import os
gameName = raw_input("please input gameName:", )
channelName = raw_input("please input channelName:", )

def getPackagName():
    cmd = 'adb shell pm list packages | findstr \"' + gameName + '\" | findstr \"' + channelName + '\"'
    resultGet = os.popen(cmd).read()
    listStr = resultGet.split()
    subStr=listStr[0].split(":",1)
    return subStr[-1]

def getDeviceID():
    cmd="adb devices"
    resultGet=os.popen(cmd).read()
    listStr=resultGet.split("\n")
    subList=listStr[1].split("\t")
    return subList[0]