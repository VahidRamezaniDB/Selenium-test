from selenium import webdriver
from selenium.webdriver.common.by import By
import time

TEST_DESCRIPTION = "Test #11\nThis test case checks if a picture is displayed.\n\n"
DELIMITER = "-----------------------------------------------------\n\n"
PASSED = "Passed.\n\n"
FAILED = "Failed.\n\n"

def test11(driver):
    about_us = driver.find_element(By.XPATH, "/html/body/div/nav/div/ul/li[2]/a")
    about_us.click()
    time.sleep(1)
    elem = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div/div/div/div/div[2]/figure[5]/img")
    try:
        assert elem.is_displayed()
        with open("OutLog.txt", 'at') as out_file:
            out_file.write(TEST_DESCRIPTION)
            out_file.write(PASSED)
            out_file.write(DELIMITER)
    except AssertionError as e:
        with open("OutLog.txt", 'at') as out_file:
            out_file.write(TEST_DESCRIPTION)
            out_file.write(FAILED)
            out_file.write(DELIMITER)