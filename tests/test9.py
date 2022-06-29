from selenium import webdriver
from selenium.webdriver.common.by import By

TEST_DESCRIPTION = "Test #9\nThis test case checks the down-arrow element in the first page.\n\n"
DELIMITER = "-----------------------------------------------------\n\n"
PASSED = "Passed.\n\n"
FAILED = "Failed.\n\n"

def test9(driver):
    elem = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div/div/a/figure")
    try:
        assert elem.is_displayed() == True
        with open("OutLog.txt", 'at') as out_file:
            out_file.write(TEST_DESCRIPTION)
            out_file.write(PASSED)
            out_file.write(DELIMITER)
    except AssertionError as e:
        with open("OutLog.txt", 'at') as out_file:
            out_file.write(TEST_DESCRIPTION)
            out_file.write(FAILED)
            out_file.write(DELIMITER)