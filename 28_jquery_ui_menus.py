from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)

# driver.find_element(By.XPATH,"//a[normalize-space()='JQuery UI Menus']").click()
driver.find_element(By.XPATH,"//a[text()='JQuery UI Menus']").click()
time.sleep(1)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH,"//a[normalize-space()='Enabled']")).perform()
time.sleep(1)

driver.find_element(By.XPATH,"//a[text()='Back to JQuery UI']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//a[text()='JQuery UI']").click()
time.sleep(1)

driver.back()
time.sleep(1)

driver.find_element(By.XPATH,"//a[text()='Menu']").click()
time.sleep(1)

action.move_to_element(driver.find_element(By.XPATH,"//a[normalize-space()='Enabled']")).perform()
time.sleep(1)

action.move_to_element(driver.find_element(By.XPATH,"//a[text()='Downloads']")).perform()
time.sleep(1)

driver.find_element(By.XPATH,"//a[text()='PDF']").click()
time.sleep(2)

print("pass")



















