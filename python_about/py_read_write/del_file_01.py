#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""递归删除文件夹"""
import shutil
import os
# shutil.rmtree('C:\\test_01\\test_02\\')

"""删除指定文件夹"""
import os
def scanfile(startscan, target) :
    """函数startscan的形参target可以是目录名也可以是文件名"""
    os.chdir(startscan)# 函数chdir的作用是切换到指定目录
    for obj in os.listdir(os.curdir):
        if obj == target:
            print os.getcwd() +os.sep +obj
        if os.path.isdir(obj):
            scanfile(obj,target)
            os.chdir(os.pardir)#返回上层目录

startscan = raw_input("Please input startscan:")
target = raw_input("Please input target:")
scanfile(startscan,target)

# int[] items =  new int[]{1,3,5,7,9,2,4,6,8}


import os
def removeDir(dirPath):
    if not os.path.isdir(dirPath):
        return
    files = os.listdir(dirPath)
    try:
        for file in files:
            filePath = os.path.join(dirPath,file)
            if os.path.isfile(filePath):
                os.remove(filePath)
            elif os.path.isdir(filePath):
                 removeDir(filePath)
        os.rmdir(dirPath)
    except Exception, e:
        print e


if __name__ == '__main__':
    removeDir('/data/python/t')