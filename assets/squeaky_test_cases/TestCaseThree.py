# Squeaky Clean Project
# Author: Neha Koduru
# version: 1.1
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_verifyContactUsServicesPagewithLogoutScenario(self):
        username = "admin"
        pwd = "admin"
        address = "122 Street"
        phone = "2345678"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://niharika9.pythonanywhere.com/")
        time.sleep(2)
        element = driver.find_element(By.XPATH, "//a[contains(text(), 'My account')]")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        element = driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]")
        driver.execute_script("arguments[0].click();", element)

        driver.find_element(By.ID, "id_username").send_keys(username)
        driver.find_element(By.ID, "id_password").send_keys(pwd)
        time.sleep(2)
        submit_button = driver.find_element(By.XPATH, "//input[@value='login']")
        submit_button.click()
        print("-----------------------------------------------------------------------")
        print("User has successfully logged in to an application..!")
        time.sleep(3)
        print("-----------------------------------------------------------------------")
        print("User has successfully logged in to an application..!")
        time.sleep(3)
        element = driver.find_element(By.XPATH, "//a[contains(., 'About')]")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        element = driver.find_element(By.XPATH, "//a[contains(text(), 'Who we are')]")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        headerone = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/h1").text
        print(headerone)
        print("User in on Who We Are page...")
        print("-----------------------------------------------------------------------")
        driver.back()
        element = driver.find_element(By.XPATH, "//a[contains(., 'About')]")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        element =  driver.find_element(By.XPATH, "//a[contains(., 'Services')]")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        headertwo = driver.find_element(By.XPATH, "/html/body/div[3]/h2").text
        headerthree = driver.find_element(By.XPATH, "/html/body/div[3]/p").text
        headerfour = driver.find_element(By.XPATH, "/html/body/div[4]/h2").text
        print(headertwo)
        print("-----------------------------------------------------------------------")
        print(headerthree)
        print("-----------------------------------------------------------------------")
        print(headerfour)
        print("-----------------------------------------------------------------------")
        headersix = driver.find_element(By.XPATH, "/html/body/div[6]/p").text
        print(headersix)
        headerseven =  driver.find_element(By.XPATH, "/html/body/div[6]/h2").text
        print(headerseven)
        driver.back()
        element = driver.find_element(By.XPATH, "//a[contains(., 'About')]")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        element = driver.find_element(By.XPATH, "//a[contains(., 'Contact us')]")
        driver.execute_script("arguments[0].click();", element)
        headereight = driver.find_element(By.XPATH, "/html/body/h2").text
        print(headereight)
        print("-----------------------------------------------------------------------")
        time.sleep(2)
        element = driver.find_element(By.XPATH, "//a[contains(., 'My account')]")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        element = driver.find_element(By.XPATH, "//a[contains(., 'Logout')]")
        driver.execute_script("arguments[0].click();", element)
        headernine = driver.find_element(By.XPATH, "/html/body/div[3]/p").text
        print(headernine)
        print("You have been logged out from an application..!")

if __name__ == '__main__':
    unittest.main()
