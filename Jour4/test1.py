# _*_ coding : utf-8 _*_
# @Time : 6/7/2022 9:34 AM
# @Author : Min Li
# @File : test1
# @Project : SeleniumProjet1
import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
time.sleep(2)

driver.find_element(By.ID,"KW").send_keys("BPMN")







