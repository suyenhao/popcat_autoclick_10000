# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 19:48:21 2021

@author: su
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
PATH = "D:/su/Searches/chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://popcat.click/")

cat = driver.find_element_by_id("app")
actions = ActionChains(driver)
actions.click(cat)

for i in range(10000):
     actions.perform()
     