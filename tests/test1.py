from selenium import webdriver
from selenium.webdriver.common.by import By

TEST_DESCRIPTION = "Test #1\nThis test case checks first page element.\n\n"
DELIMITER = "-----------------------------------------------------\n\n"
PASSED = "Passed.\n\n"
FAILED = "Failed.\n\n"

driver = webdriver.Chrome()
driver.get("https://www.partsoftware.com/")
elem = driver.find_element(By.XPATH, "/html/body/div/main/section[1]/div[2]/h1")
try:
    assert "طــراح" in elem.text
    with open("OutLog.txt", 'wt') as out_file:
        out_file.write(TEST_DESCRIPTION)
        out_file.write(PASSED)
        out_file.write(DELIMITER)
except AssertionError as e:
    with open("OutLog.txt", 'wt') as out_file:
        out_file.write(TEST_DESCRIPTION)
        out_file.write(FAILED)
        out_file.write(DELIMITER)
finally:
    driver.close()    
