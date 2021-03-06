#!/usr/bin/env python3
#coding:utf-8
import logging
import os
import time
import shutil
class Logger(object):
    def __init__(self,logger):
        """指定保存日志的文件路径，日志级别及调用文件，将日志存入到指定的文件中"""
        #创建一个logger
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)#设置最底层筛选级别（级别NOTSET<DEBUG<INFO<WARNING<ERROR<FATAL，级别往右越高），筛选级别出大于等于DEBUG的log

        #可直接使用logging.basicConfig()，这是一个logging提供的一个简单的配置方法，使用该方法不用自己添加handler，如果要自定义log方法，则手动添加handler
        #创建一个handler，用于写入日志到文件
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))#定义log文件标题中时间的显示格式

        # 如果目录不存在，则创建新目录
        if not os.path.exists(os.path.dirname(os.getcwd()) + '/Logs'):
            # shutil.rmtree(os.path.dirname(os.getcwd()) + '/Logs')#如果目录已存在，可以删除目录（import shutil;shutil.rmtree（path）可用于删除非空目录）。删除空目录(单级目录)用os.rmdir(path)或（多级目录）os.removedirs(paht)
            os.mkdir(os.path.dirname(os.getcwd()) + '/Logs')
        # os.removedirs(os.path.dirname(os.getcwd())+'/Logs')#删除文件夹
        log_path = os.path.dirname(
            os.getcwd()) + '/Logs/'  # os.getcwd()得到当前执行的py文件所在的目录（SeleniumTest/csdn），用os.path.dirname(path）获取当前模块所在的目录（SeleniumTest）。
        # 另一种获取目录（绝对路径）的方式：os.abspath()
        log_name = log_path + rq + '.log'  # os.remove(file)删除文件

        fh = logging.FileHandler(log_name)  # os.mknod("test.txt")创建空文件；fp = open("test.txt",w) 直接打开一个文件，如果文件不存在则创建文件
        fh.setLevel(logging.INFO)  #设置第二层筛选器，筛选出INFO级别及以上的日志到日志文件中

        #再创建一个handler,用于把log输出到控制台
        ch=logging.StreamHandler()#StreamHandler，用于控制台输出的handler
        ch.setLevel(logging.DEBUG)#设置第二层筛选器，筛选出DEBUG级别及以上级别的日志输出到控制台中

        #定义handle的输出格式
        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')#设置log的格式：当前时间-当前类名-日志级别-日志信息
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #给logger添加定义好的handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        # 本写法无需添加移除handler的这种做法！！！！
        #移除添加的handler，防止logging重复写日志
        # logger.removeHandler(fh)
        # logger.removeHandler(ch)
        #

    def getLog(self):
        return self.logger