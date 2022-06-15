# _*_ coding : utf-8 _*_
# @Time : 6/13/2022 7:42 PM
# @Author : Min Li
# @File : GestionAlerte
# @Project : SeleniumProjet1
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Trouver le boutton Click for JS Alert
driver.find_element(By.XPATH,"//button[contains(text(),'Alert')]").click()

# Récupérer l'alerte à l'aide d'une variable dans le cas d'utilisation répétée
alertWindow = driver.switch_to.alert
# Afficher l'alerte dans la console
print(alertWindow.text)

# Cliquer sur le bouton OK de l'alerte(dismiss = cancel)
alertWindow.accept()

time.sleep(4)

# Fermer toutes les fenetres ouvertes manipulée par le script; driver.close()---->fermer 1 seule fenetre
driver.quit()