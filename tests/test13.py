import time
from selenium import webdriver
from selenium.webdriver.common.by import By

TEST_DESCRIPTION = "Test #13\nThis test case checks if an event's title is displayed correctly.\n\n"
DELIMITER = "-----------------------------------------------------\n\n"
PASSED = "Passed.\n\n"
FAILED = "Failed.\n\n"

def test13(driver):
    events = driver.find_element(By.XPATH, "/html/body/div/nav/div/ul/li[4]/a")
    events.click()
    time.sleep(1)
    elem = driver.find_element(By.XPATH, "/html/body/div/main/div[4]/div/div/div/div[2]/div[2]/a[1]/p")
    try:
        assert "هفدهمین دوره کالج پارت- YOU.I" in elem.text
        with open("OutLog.txt", 'at') as out_file:
            out_file.write(TEST_DESCRIPTION)
            out_file.write(PASSED)
            out_file.write(DELIMITER)
    except AssertionError as e:
        with open("OutLog.txt", 'at') as out_file:
            out_file.write(TEST_DESCRIPTION)
            out_file.write(FAILED)
            out_file.write(DELIMITER)