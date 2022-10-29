import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pageObjects.Loginpage import LoginPage


class Test_001_Login:
    baseURL = 'https://admin-demo.nopcommerce.com/'
    username = "admin@yourstore.com"
    password = "admin"

    def test_homepagetitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login1":
            print("actual_title is matched")
        else:
            self.driver.save_screenshot("C:\\Users\\DELL\\PycharmProjects"
                                        "\\pom-project\\Screenshots"+"test_homepagetitle.png")
            print("home page title is not matched")
        self.driver.close()

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.enterusername(self.username)
        time.sleep(1)
        self.lp.enterpassword(self.password)
        time.sleep(1)
        self.lp.clicklogin()
        time.sleep(3)
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            print("dashboard is matched")
        else:
            print("page isn't matched")
        self.lp.clicklogout()
        self.driver.close()





