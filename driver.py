import os
import time

for i in range(10):
    os.system("python tests/test" + str(i) + ".py")
    time.sleep(2)