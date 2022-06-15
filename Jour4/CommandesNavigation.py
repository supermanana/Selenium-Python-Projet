# _*_ coding : utf-8 _*_
# @Time : 6/1/2022 7:28 PM
# @Author : Min Li
# @File : commandesGenerales
# @Project : SeleniumProjet
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

#Obtenir url de la page
driver.get("https://demo.nopcommerce.com/")
time.sleep(2)

driver.get("http://www.google.com")
time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()
time.sleep(3)

driver.quit()