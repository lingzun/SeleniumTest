#!/usr/bin/python3
#conding:utf-8
from test1.logger import Logger
import os
import time

mylog = Logger(logger='BasePage').getLog()
class BasePage(object):
    """主要把selenium中几个常用的方法封装到BasePage类中，这里演示了几个方法"""
    """back(),forward(),get(),quit()"""
    def __init__(self,driver):
        """构造函数，有一个参数，driver"""
        self.driver=driver

    def back(self):
        #后退操作
        self.driver.back()
        mylog.info("后退")

    def forward(self):
        #前进操作
        self.driver.forward()
        mylog.info("前进")
    def open_url(self,url):
        #进入某个url网址
        self.driver.get(url)
        mylog.info("打开网页链接：" + url)

    def quit_browser(self):
        #退出浏览器
        self.driver.quit()
        mylog.info("退出浏览器")

    def take_screenshot(self):
        file_path = os.path.dirname(os.getcwd()) + '/Screenshots/'
        if not os.path.exists(file_path):
            os.mkdir(file_path)
            mylog.info("截图文件夹不存在，执行创建截图文件夹操作")
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        if os.path.exists(screen_name):
            os.remove(screen_name)
            mylog.info("截图文件已存在，执行文件删除操作")
        try:
            self.driver.get_screenshot_as_file(screen_name)
            mylog.info("执行截图并保存操作")

        except Exception as e:
            mylog.error("出现异常：", format(e))
