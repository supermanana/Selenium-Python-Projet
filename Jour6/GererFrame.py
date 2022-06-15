# _*_ coding : utf-8 _*_
# @Time : 6/13/2022 9:04 PM
# @Author : Min Li
# @File : Exercice1
# @Project : SeleniumProjet1

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

# Entrer dans la frame(par ID, NAME, or WEBNAME)
driver.switch_to.frame("packageListFrame")

time.sleep(3)

#Cliquer sur le lien
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()

# Quittet la 1e frame, retourner a la page principale
driver.switch_to.default_content()

# Entrer dans la 2e frame
driver.switch_to.frame("packageFrame")

#driver.find_element(By.XPATH,"/html/body/main/div/section[1]/ul/li[14]/a/span").click()
driver.find_element(By.XPATH,"//a/span[text()='WebDriver']").click()
time.sleep(3)

#Sortir du 2e frame et retourner ] la page principale
driver.switch_to.default_content()

#Entrer dans la 3e frame
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()
time.sleep(3)

driver.quit()


