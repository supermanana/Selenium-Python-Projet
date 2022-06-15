import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# 1) Ouvrir le navigateur(chrome/firefox/Edge)
driver = webdriver.Chrome()
# 2) Naviguer vers l'url https://bdeb.omnivox.ca/Login/Account/Login?ReturnUrl=%2fintr
driver.get("https://www.amazon.ca/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.ca%2Fgp%2Fcss%2Fhomepage.html%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=caflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
# 3) Entrer username
driver.find_element(By.ID, "ap_email").send_keys("merci_520@hotmail.com")
# 4) Cliquer sur le bouton Continue
driver.find_element(By.ID, "continue").click()
# 5) Entrer password
driver.find_element(By.ID, "ap_password").send_keys("Syncmaster500b")
# 6) Cliquer sur le bouton Sign in
driver.find_element(By.ID, "signInSubmit").click()
# 7) recuperer le titre de la page(titre actuel)
act_title = driver.title
# 8) Verifier le titre de la page: Amazon Sign In (attendu)
exp_title = "Amazon Sign In"
# exp_msg_error = driver.find_element(By.ID,"error").text
# print("Le message d'erreur est : "+exp_msg_error)
if act_title == exp_title:
    print("Le test Login  est passed")
    print("Le titre de la page est : " + act_title)
else:
    print("Le test Login  est failed")
time.sleep(4)
# 8) Fermer le navigateur
driver.close()