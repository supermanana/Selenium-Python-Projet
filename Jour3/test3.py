# _*_ coding : utf-8 _*_
# @Time : 5/30/2022 11:30 PM
# @Author : Min Li
# @File : test3
# @Project : SeleniumProjet1

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#1) Ouvrir le navigateur(chrome/firefox/Edge)
driver = webdriver.Chrome()
# 2) Naviguer vers l'url https://saucedemo.com/
driver.get("https://saucedemo.com/")
# 3) Maximiser la fenêtre
driver.maximize_window()
# 4) Entrer username (standard_user)
driver.find_element(By.NAME,"user-name").send_keys("standard_user")
#driver.find_element(By.ID,"user-name").send_keys("standard_user")
# 5) Entrer password (secret_sauce)
driver.find_element(By.ID,"password").send_keys("secret_sauce")
# 6) Cliquer sur le bouton Login
#driver.find_element(By.NAME,"login-button").click()
driver.find_element(By.XPATH,"(//input[@type='submit'])[1]").click()
# 7) Ajouter le premier article dans le panier
#driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
#driver.find_element(By.XPATH, "(//button[@class='btn btn_primary btn_small btn_inventory'])[1]").click()
driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
time.sleep(2)
# 8) Cliquer le panier
driver.find_element(By.CLASS_NAME,"shopping_cart_badge").click()
time.sleep(2)
# 9) Cliquer le bouton Checkout
driver.find_element(By.ID,"checkout").click()
time.sleep(2)
# 10) Cliquer le bouton Cancel
driver.find_element(By.NAME,"cancel").click()
time.sleep(2)
# 11) Cliquer le bouton Remove
driver.find_element(By.NAME,"remove-sauce-labs-backpack").click()
time.sleep(4)
# 12) Fermer la fenêtre
driver.quit()

