from selenium import webdriver
from selenium.webdriver.common.by import By
import time

TEST_DESCRIPTION = "Test #12\nThis test case checks if a picture which will be visible only by swiping is displayed after swiping.\n\n"
DELIMITER = "-----------------------------------------------------\n\n"
PASSED = "Passed.\n\n"
FAILED = "Failed.\n\n"


def test12(driver):
    products = driver.find_element(By.XPATH, "/html/body/div/nav/div/ul/li[3]/a")
    products.click()
    time.sleep(1)
    next_slide = driver.find_element(By.XPATH, "/html/body/div/main/div[3]/div[4]/ul/li[4]/a/span[2]")
    next_slide.click()
    time.sleep(1)
    picture_elem = driver.find_element(By.XPATH, "/html/body/div/main/div[3]/div[1]/div/div[4]/div/div/figure/img")
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
