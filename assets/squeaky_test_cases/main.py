# Squeaky Clean Project
# Author: Neha Koduru
# version: 1.1
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestCase_One(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_verifyHomepageAndSignUpScenario(self):
        username = "Tommy"
        pwd = "Murdock"
        firstname = "Tom"
        lastname = "Murdock"
        email = "Rom1@gmail.com"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://niharika9.pythonanywhere.com")
        time.sleep(2)
        headerone = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/p/strong").text
        print("User has successfully logged in to an application..!")
        print("-----------------------------------------------------------------------")
        print(headerone)
        headertwo = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/div/div/h5").text
        print("-----------------------------------------------------------------------")
        print(headertwo)
        headerthree = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div/a").text
        print(headerthree)
        print("-----------------------------------------------------------------------")
        time.sleep(2)
        element = driver.find_element(By.XPATH, "//a[contains(text(), 'Get started')]")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        element = driver.find_element(By.XPATH, "//a[contains(text(), 'Sign up')]")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[3]/form/input[2]").send_keys(username)
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[3]/form/input[3]").send_keys(firstname)
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[3]/form/input[4]").send_keys(lastname)
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[3]/form/input[5]").send_keys(pwd)
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[3]/form/input[6]").send_keys(email)
        time.sleep(2)

        element = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
        element.click()
        time.sleep(3)
        submit_button = driver.find_element(By.XPATH, "//input[@value='login']")
        submit_button.click()

        driver.find_element(By.ID, "id_username").send_keys(username)
        driver.find_element(By.ID, "id_password").send_keys(pwd)
        time.sleep(2)
        submit_button = driver.find_element(By.XPATH, "//input[@value='login']")
        submit_button.click()
        print("-----------------------------------------------------------------------")
        print("User has successfully logged in to an application..!")
        time.sleep(3)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main(warnings='ignore')