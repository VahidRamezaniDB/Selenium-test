from selenium import webdriver
from selenium.webdriver.common.by import By

TEST_DESCRIPTION = "Test #1\nThis test case checks first page element.\n"

driver = webdriver.Chrome()
driver.get("https://www.partsoftware.com/")
elem = driver.find_element(By.XPATH, "/html/body/div/main/section[1]/div[2]/h1")
try:
    assert "طــراح" in elem.text
    print("passed.")
    print(TEST_DESCRIPTION)
except AssertionError as e:
    print("rejected")
finally:
    driver.close()    
