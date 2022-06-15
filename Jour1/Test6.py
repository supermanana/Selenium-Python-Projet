import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# 1) Ouvrir le navigateur(chrome/firefox/Edge)
driver = webdriver.Chrome()
# 2) Naviguer vers l'url
driver.get("https://www.fossil.com/fr-ca/login/")
# 3) Entrer username
driver.find_element(By.ID, "login-form-email").send_keys("merci_520@hotmail.com")
# 5) Entrer password
driver.find_element(By.ID, "login-form-password").send_keys("Syncmaster500b.")
# 6) Cliquer sur le bouton Sign in
driver.find_element(By.XPATH, "(//*[@id='login']/div/div[2]/form/button)").click()
# 7) recuperer le titre de la page(titre actuel)
act_title = driver.title
# 8) Verifier le titre de la page: Sites-fossil-ca-Site (attendu)
exp_title = "Sites-fossil-ca-Site"
# exp_msg_error = driver.find_element(By.ID,"error").text
# print("Le message d'erreur est : "+exp_msg_error)
if act_title == exp_title:
    print("Le test Login  est passed")
    print("Le titre de la page est : " + act_title)
else:
    print("Le test Login  est failed")
time.sleep(10)
# 8) Fermer le navigateur
driver.quit()