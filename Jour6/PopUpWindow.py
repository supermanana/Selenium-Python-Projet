# _*_ coding : utf-8 _*_
# @Time : 6/13/2022 8:48 PM
# @Author : Min Li
# @File : PopUpWindow
# @Project : SeleniumProjet1
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

#driver.get("https://the-internet.herokuapp.com/basic_auth")

# Envoyer le login et le mot de passe: admin pour contourner
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

time.sleep(3)

driver.quit()