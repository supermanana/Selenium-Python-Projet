# _*_ coding : utf-8 _*_
# @Time : 6/13/2022 11:33 PM
# @Author : Min Li
# @File : Exercice2
# @Project : SeleniumProjet1
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("http://demo.automationtesting.in/Frames.html")

driver.find_element(By.XPATH,"/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[1]/a").click()

#driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("Bonjour")

driver.switch_to.frame("SingleFrame")

driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("Bonjour")

driver.switch_to.default_content()

driver.find_element(By.XPATH,"/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()

driver.switch_to.frame(driver.find_element(By.XPATH,("//iframe[contains(@src,'MultipleFrames')]")))
driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("salut")

time.sleep(5)
driver.quit()