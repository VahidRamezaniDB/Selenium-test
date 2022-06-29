import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.test1 import *
from tests.test2 import *
from tests.test3 import *
from tests.test4 import *
from tests.test5 import *
from tests.test6 import *
from tests.test7 import *
from tests.test8 import *
from tests.test9 import *
from tests.test10 import *
from tests.test11 import *
from tests.test12 import *
from tests.test13 import *
from tests.test14 import *
from tests.test15 import *
from tests.test16 import *
from tests.test17 import *


test_set = [test1, test2, test3, test4, test5, test6, test7, test8, test9,
            test10, test11, test12, test13, test14, test15, test16, test17]
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.partsoftware.com/")


for test in test_set:
    test(driver=driver)

driver.close()