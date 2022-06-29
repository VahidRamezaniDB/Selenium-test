from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def test15(driver):
    TEST_DESCRIPTION = "Test #15\nThis test case checks if the title in cooperation is correctly displayed.\n\n"
    DELIMITER = "-----------------------------------------------------\n\n"
    PASSED = "Passed.\n\n"
    FAILED = "Failed.\n\n"

    cooperation = driver.find_element(By.XPATH, "/html/body/div/nav/div/ul/li[6]/a")
    cooperation.click()
    time.sleep(1)
    elem = driver.find_element(By.XPATH, "/html/body/div/main/div[6]/div[1]/div/div[1]/div/div/h2")
    try:
        assert "همکاری با خانواده بزرگ پارت"==elem.text
        with open("OutLog.txt", 'at') as out_file:
            out_file.write(TEST_DESCRIPTION)
            out_file.write(PASSED)
            out_file.write(DELIMITER)
    except AssertionError as e:
        with open("OutLog.txt", 'at') as out_file:
            out_file.write(TEST_DESCRIPTION)
            out_file.write(FAILED)
            out_file.write(DELIMITER)