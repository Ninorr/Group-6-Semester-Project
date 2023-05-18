# Squeaky Clean Project
# Author: Neha Koduru
# version: 1.1
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCase_Two(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_placeAnOrderAndVerifyOrderHistoryScenario(self):

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
        driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div/a").click()
        time.sleep(2)
        headerfour = driver.find_element(By.XPATH, "/html/body/div[3]/h1").text
        print(headerfour)
        print("-----------------------------------------------------------------------")
        driver.find_element(By.XPATH, "//a[contains(., 'Start my order')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[3]/div[2]/form/div/input").click()
        headerfive = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[3]/div[2]/div/div").text
        print(headerfive)
        print("-----------------------------------------------------------------------")
        print("Your selected item has been added to the cart..!!")
        element = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/ul/li[5]/a")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        print("-----------------------------------------------------------------------------------")
        element = driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element(By.XPATH, "/html/body/div[3]/div/a")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        element = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/form/div[1]/input").send_keys(address)
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/form/div[2]/input").send_keys(phone)
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/form/input[2]").click()
        time.sleep(2)
        headerseven = driver.find_element(By.XPATH, "/html/body/div[3]/p[1]").text
        print(headerseven)


if __name__ == '__main__':
    unittest.main()
