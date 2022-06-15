# _*_ coding : utf-8 _*_
# @Time : 6/2/2022 9:52 AM
# @Author : Min Li
# @File : Exercice
# @Project : SeleniumProjet1
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("http://www.google.ca")

driver.find_element(By.XPATH, "(//input[@name='q'])").send_keys("selenium")

time.sleep(2)

#driver.find_element(By.XPATH,"(/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/ul[1]/div/ul/li[3]/"

#                           "div/div[2]/div[1]/span/b)").click()
drop_liste =  driver.find_element(By.ID,"input-country")

liste = Select(drop_liste)

#liste.select_by_visible_text("selenium webdriver")

all_listes = liste.options
total_liste = len(all_listes)

for opt in all_listes:
    if opt.text == "selenium webdriver":
        opt.click()
        break

time.sleep(2)

driver.quit()


