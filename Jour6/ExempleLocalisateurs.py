# _*_ coding : utf-8 _*_
# @Time : 6/15/2022 10:31 AM
# @Author : Min Li
# @File : ExempleLocalisateurs
# @Project : SeleniumProjet1
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver.get("http://www.amazon.ca/")
#driver.find_element(By.ID,"nav-search-submit-button").click()
#time.sleep(2)
#driver.find_element(By.ID,"nav-logo-sprites").click()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.NAME,"txtUsername").send_keys("Admin")
driver.find_element(By.NAME,"txtPassword").send_keys("admin123")
driver.find_element(By.CLASS_NAME,"button").click()

#driver.get("http://www.baidu.com/")
#driver.find_element(By.ID,"kw").send_keys("NI hao")

driver.find_element(By.CSS_SELECTOR,".firstLevelMenu").click()

driver.find_element(By.LINK_TEXT,"Job").click()
time.sleep(3)
driver.quit()