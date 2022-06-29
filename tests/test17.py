from selenium import webdriver
from selenium.webdriver.common.by import By
import time

TEST_DESCRIPTION = "Test #17\nThis test case checks if the correct alert is displayed after entering invalid name.\n\n"
DELIMITER = "-----------------------------------------------------\n\n"
PASSED = "Passed.\n\n"
FAILED = "Failed.\n\n"

def test17(driver):
    contact_us = driver.find_element(By.XPATH, "/html/body/div/nav/div/ul/li[7]/a")
    contact_us.click()
    time.sleep(1)
    fullname_textfield = driver.find_element(By.XPATH, "/html/body/div/main/div[7]/div/div/div/form/div[1]/input")
    try:
        fullname_textfield.send_keys("123")
        submit = driver.find_element(By.XPATH, "/html/body/div/main/div[7]/div/div/div/form/button")
        driver.execute_script("arguments[0].click();", submit)
        time.sleep(1)
        alert = driver.find_element(By.XPATH, "/html/body/div/main/div[7]/div/div/div/form/div[1]/span")
        assert alert.is_displayed()
        with open("OutLog.txt", 'wt') as out_file:
            out_file.write(TEST_DESCRIPTION)
            out_file.write(PASSED)
            out_file.write(DELIMITER)
    except AssertionError as e:
        with open("OutLog.txt", 'wt') as out_file:
            out_file.write(TEST_DESCRIPTION)
            out_file.write(FAILED)
            out_file.write(DELIMITER)