#!/usr/bin/env python3
# coding:utf-8
import time, unittest
from selenium import webdriver


class BaiduSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)

    def tearDown(self):
        self.driver.quit()

    def test_baidu_search(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium")
        time.sleep(5)
        self.driver.find_element_by_id("kw").clear()
        time.sleep(3)
        try:
            assert 'selenium' in self.driver.title
            print("Test pass!")
        except Exception as e:
            print("Test fail!", format(e))


if __name__ == "__main__":
    unittest.main()
