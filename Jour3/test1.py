# _*_ coding : utf-8 _*_
# @Time : 5/30/2022 8:37 PM
# @Author : Min Li
# @File : test1
# @Project : SeleniumProjet1
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 1) Ouvrir le navigateur(chrome/firefox/Edge)
driver = webdriver.Chrome()
# 2) Naviguer vers l'url https://opensource-demo.orangehrmlive.com/
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(2)
# 3) Utiliser le localisateur--link text: a
#driver.find_element(By.CLASS_NAME, "ico-register").click()
#driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Regi").click()
time.sleep(2)

driver.find_element(By.ID,"FirstName").send_keys("Min")
driver.find_element(By.NAME,"LastName").send_keys("LI")
driver.find_element(By.ID,"Email").send_keys("123@hotmail.com")
driver.find_element(By.NAME,"Password").send_keys("12345678")
driver.find_element(By.ID,"ConfirmPassword").send_keys("12345678")
driver.find_element(By.NAME,"register-button").click()
time.sleep(2)
driver.quit()


# # 4) Entrer password (admin123)
# driver.find_element(By.ID, "txtPassword").send_keys("admin123")
# # 5) Cliquer sur le bouton Login
# driver.find_element(By.ID, "btnLogin").click()
# # 6) recuperer le titre de la page(titre actuel)
# act_title =  driver.title
# # 7) Verifier le titre de la page: OrangeHRM  (attendu)
# exp_title = "OrangeHRM"
# if act_title == exp_title:
#     print("Le test Login  est passed")
# else:
#     print("Le test Login  est failed")
# time.sleep(10)  # mecanisme d'attendre dynamique
# # 8) Fermer le navigateur
# driver.close()