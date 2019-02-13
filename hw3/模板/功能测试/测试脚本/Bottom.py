# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Bottom(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.vipbcw.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_bottom(self):
        driver = self.driver
        driver.get(self.base_url + "/main/index.html")
        driver.find_element_by_xpath(u"(//a[contains(text(),'百草味APP')])[2]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'新闻中心')])[2]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'品牌介绍')])[2]").click()
        driver.find_element_by_link_text(u"团购好礼").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'热卖单品')])[2]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'美味中心')])[2]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'礼金卡')])[2]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'客服帮助')])[2]").click()
        driver.find_element_by_link_text(u"517吃货节").click()
        driver.find_element_by_link_text(u"男神来了").click()
        driver.find_element_by_link_text(u"小味公益").click()
        driver.find_element_by_link_text(u"小味快速达").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'关于我们')])[2]").click()
        driver.find_element_by_link_text(u"浙ICP备14038051号-2").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
