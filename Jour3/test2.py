# _*_ coding : utf-8 _*_
# @Time : 5/30/2022 9:13 PM
# @Author : Min Li
# @File : test2
# @Project : SeleniumProjet1
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#  Utiliser le localisateur--link text: a
#driver.find_element(By.CLASS_NAME, "ico-register").click()
#driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.CLASS_NAME,"ico-login").click()


driver.find_element(By.ID,"Email").send_keys("123@hotmail.com")
driver.find_element(By.NAME,"Password").send_keys("12345678")

# XPATH: chemin relatif
driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
time.sleep(2)
driver.quit()