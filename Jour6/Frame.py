# _*_ coding : utf-8 _*_
# @Time : 6/13/2022 8:52 PM
# @Author : Min Li
# @File : Frame
# @Project : SeleniumProjet1
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("")