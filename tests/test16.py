from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def test16(driver):
    TEST_DESCRIPTION = "Test #16\nThis test case checks if a picture in 'Contact us' section is displayed.\n\n"
    DELIMITER = "-----------------------------------------------------\n\n"
    PASSED = "Passed.\n\n"
    FAILED = "Failed.\n\n"

    contact_us = driver.find_element(By.XPATH, "/html/body/div/nav/div/ul/li[7]/a")
    contact_us.click()
    time.sleep(1)
    picture_elem = driver.find_element(By.XPATH, "/html/body/div/main/div[7]/div/div/div/figure/img")
    try:
        assert picture_elem.is_displayed()
        with open("OutLog.txt", 'wt') as out_file:
            out_file.write(TEST_DESCRIPTION)
            out_file.write(PASSED)
            out_file.write(DELIMITER)
    except AssertionError as e:
        with open("OutLog.txt", 'wt') as out_file:
            out_file.write(TEST_DESCRIPTION)
            out_file.write(FAILED)
            out_file.write(DELIMITER)