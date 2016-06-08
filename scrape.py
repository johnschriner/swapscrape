import sys
import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, re


uploadfile = random.choice(os.listdir("path/to/image/files/dir"))
###print(uploadfile)
path = "/path/to/image/files/dir" + str(uploadfile)
###print(path)

class FirstpartTry3Best(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "~~~BASE URL HERE~~~~"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_firstpart_try3_best(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        self.driver.implicitly_wait(5)
	driver.find_element_by_id("agree").click()
        driver.find_element_by_name("picture").clear()
	driver.find_element_by_name("picture").send_keys(path)
        self.driver.implicitly_wait(8)
        driver.find_element_by_id("fakeUpload").click()
        WholeURL = driver.current_url
        print WholeURL       
	ending = WholeURL.rsplit('/', 1)[-1]
	ending = str(int(ending) - 8)
	for x in range(8):
        	os.system("image-scraper ~~~~PLACE URL HERE~~~~" + ending + " --formats gif jpg jpeg")
        	time.sleep(3)
		ending = str(int(ending)+1)
        	print(ending)	



    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()


