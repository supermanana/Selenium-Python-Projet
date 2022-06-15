import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Trouver le boutton Click for JS Alert
driver.find_element(By.XPATH,"//button[contains(text(),'Confirm')]").click()

time.sleep(3)

confirmWindow = driver.switch_to.alert

print(confirmWindow.text)

confirmWindow.dismiss()

time.sleep(3)

driver.quit()