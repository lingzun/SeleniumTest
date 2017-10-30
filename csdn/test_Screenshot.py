#!/usr/bin/env python3
# coding:utf-8
import time
from selenium import webdriver
from test1.base_page import BasePage


class TestScreenshot(object):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(8)
    basepage = BasePage(driver)

    def take_screenshot(self):
        self.basepage.open_url("https://www.baidu.com")
        time.sleep(5)
        self.basepage.take_screenshot()
        time.sleep(5)
        self.basepage.quit_browser()


test = TestScreenshot()
test.take_screenshot()
