# _*_ coding : utf-8 _*_
# @Time : 6/8/2022 10:02 PM
# @Author : Min Li
# @File : Exercice
# @Project : SeleniumProjet1

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("http://omayo.blogspot.com/")

drop_multiBox =  driver.find_element(By.ID,"multiselect1")

box = Select(drop_multiBox)

# box.select_by_value("volvox")
# box.select_by_value("audix")

box.select_by_visible_text("Swift")
box.select_by_visible_text("Hyundai")
time.sleep(2)

box.deselect_all()
time.sleep(2)

drop_letters = driver.find_element(By.NAME,"SiteMap")
letters = Select(drop_letters)

#letters.select_by_visible_text("doc 1")
letters.select_by_value("ghi")
time.sleep(2)


# all_options = box.options
# total_option = len(all_options)
# print(total_option)

# for opt in all_options:
#     if opt.text== "Volvo" :
#         opt.click()
#         break
#
# for opt in all_options:
#     if opt.text == "Audi":
#         opt.click()
#         break
#
driver.quit()

