# _*_ coding : utf-8 _*_
# @Time : 6/15/2022 6:11 PM
# @Author : Min Li
# @File : GestionMultiFenetre
# @Project : SeleniumProjet1
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

# Mettre le driver 1e fenetre d'une variable
driver.maximize_window()

#L'identifiant de la 1e fenetre : CDwindow-80D86D3FDEE2CEC6237DA7756ACD9376
parentWindow = driver.current_window_handle
print(parentWindow)

# Localiser le lien et le cliquer pour ouvrir la 2e fenetre
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

#Récupérer la liste des ids de fenêtres ouvertes
windowHandleIds = driver.window_handles

parentWindowId = windowHandleIds[0]
childWindowId = windowHandleIds[1]

#print(parentWindow,childWindow)

# Id, parent window: C976AE794A7F66EEE50F691231B93A22, cela change, c'est dynamique
print("parentWindowId :",parentWindowId)
print("childWindowId :",childWindowId)

# Basculer vers la 2e fenêtre, récéperer url et titre de la 2e fenêtre
driver.switch_to.window(childWindowId)
url2 = driver.current_url
title2 = driver.title
print(url2)
print(title2)
print("----------------------------------------")
driver.switch_to.window(parentWindowId)
url1 = driver.current_url
title1 = driver.title
print(url1)
print(title1)

# 2e approche
for winID in windowHandleIds:
    driver.switch_to.window(winID)
    if driver.title == title1:
        driver.close()

time.sleep(4)
driver.quit()
