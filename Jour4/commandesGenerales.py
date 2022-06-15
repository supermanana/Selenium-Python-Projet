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
url_page = driver.current_url
print(url_page)

#Obternir le titre de la page
titre_page = driver.title
print(titre_page)

#Obtenir le code source de la page
surce_page = driver.page_source
print(surce_page)

time.sleep(2)
driver.quit()

