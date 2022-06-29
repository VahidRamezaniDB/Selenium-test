from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def test14(driver):
    TEST_DESCRIPTION = "Test #14\nThis test case checks if college paragraph is correctly displayed.\n\n"
    DELIMITER = "-----------------------------------------------------\n\n"
    PASSED = "Passed.\n\n"
    FAILED = "Failed.\n\n"

    part_college = driver.find_element(By.XPATH, "/html/body/div/nav/div/ul/li[5]/a")
    part_college.click()
    time.sleep(1)
    elem = driver.find_element(By.XPATH, "/html/body/div/main/div[5]/div/div/div/div/div[2]/p[1]")

    try:
        assert "حالا چرا کالج؟ چون" in elem.text 
        with open("OutLog.txt", 'at') as out_file:
            out_file.write(TEST_DESCRIPTION)
            out_file.write(PASSED)
            out_file.write(DELIMITER)
    except AssertionError as e:
        with open("OutLog.txt", 'at') as out_file:
            out_file.write(TEST_DESCRIPTION)
            out_file.write(FAILED)
            out_file.write(DELIMITER)