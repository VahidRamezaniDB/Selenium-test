from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.partsoftware.com/")
elem = driver.find_element(By.XPATH, "/html/body/div/main/section[1]/div[2]/h1")
assert "طــراح" in elem.text
driver.close()
