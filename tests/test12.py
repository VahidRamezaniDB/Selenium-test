from selenium import webdriver
from selenium.webdriver.common.by import By

TEST_DESCRIPTION = "Test #12\nThis test case checks if a picture which will be visible only by swiping is displayed after swiping.\n\n"
DELIMITER = "-----------------------------------------------------\n\n"
PASSED = "Passed.\n\n"
FAILED = "Failed.\n\n"

driver = webdriver.Chrome()
driver.get("https://www.partsoftware.com/")
link = driver.find_element(By.XPATH, "/html/body/div/main/section[1]/figure")
actions = webdriver.ActionChains(driver)
actions.move_to_element(link)
actions.click(link)
actions.perform()
products = driver.find_element(By.XPATH, "/html/body/div/nav/ul/li[2]")
products.click()
# elem = driver.find_element(By.XPATH, "/html/body/div/main/section[3]/div/div/div[1]/div[2]/div/figure/img")
# products_actions = webdriver.ActionChains(driver)
# products_actions.click_and_hold(on_element=elem)
# products_actions.move_to_element(driver.find_element(By.XPATH, "/html/body/div/main/section[3]/div/div/div[1]/div[2]/div/div/div/p")).release()
# products_actions.perform()
# picture_elem = driver.find_element(By.XPATH, "/html/body/div/main/section[3]/div/div/div[1]/div[3]/div/figure/img")
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
finally:
    driver.close()    
