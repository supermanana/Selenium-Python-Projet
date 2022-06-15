import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# service_obj = Service("D:\\SQL\\session 3\\Automatisation des tests I\\chromedriver_win32\\chromedriver.exe")
# 1) Ouvrir le navigateur(chrome/firefox/Edge)
driver = webdriver.Chrome()
# 2) Naviguer vers l'url https://login.salesforce.com
driver.get("https://login.salesforce.com")
# driver.maximize_window()
# 3) Entrer username (min)
driver.find_element(By.ID, "username").send_keys("min")
# 4) Entrer password (min123)
driver.find_element(By.ID, "password").send_keys("min123")
# 5) Cliquer sur le bouton Se connecter
driver.find_element(By.ID, "Login").click()
# 6) recuperer le titre de la page(titre actuel)
act_title = driver.title
# print(act_title)
# 7) Verifier le titre de la page: Connexion | Salesforce  (attendu)
exp_title = "Connexion | Salesforce"
exp_msg_error = driver.find_element(By.ID,"error").text
print("Le message d'erreur est : "+exp_msg_error)
if act_title == exp_title:
    print("Le test Login  est passed")
    print("Le titre de la page est : " + act_title)
else:
    print("Le test Login  est failed")

time.sleep(4)
# 8) Fermer le navigateur
driver.close()