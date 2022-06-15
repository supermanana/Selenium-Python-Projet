# _*_ coding : utf-8 _*_
# @Time : 6/8/2022 8:47 PM
# @Author : Min Li
# @File : DropDown
# @Project : SeleniumProjet1

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.opencart.com/index.php?route=account/register")

drop_Country =  driver.find_element(By.ID,"input-country")

country = Select(drop_Country)

# Selection par texte visible(dynamique)
# country.select_by_visible_text("Canada")

# selection par index commencant par 1?
#country.select_by_index(1)

# selection par value
#country.select_by_value("45")

# Récuperer toutes les options dans le select
all_options = country.options
total_option = len(all_options)
#print("Le nombre total d'option est : ",total_option)

# afficher tous les pays dans la console
# for opt in all_options:
    #print(opt.text)

# selectionner le Canada dans les conutries et cliquer dessus
for opt in all_options:
    if opt.text == "Canada":
        opt.click()
        break




