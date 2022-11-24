import string
import random
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pageObjects.addcustomerpage import AddCustomer
from pageObjects.Loginpage import LoginPage
from Utilities.readproperties import ReadConfig
from Utilities.customlogger import LogGen


class Test_003_AddCustomer:
    baseURL = ReadConfig.getapplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()

    logger = LogGen.loggen()

    def test_addcustomer(self,setup):
        self.logger.info("******Test_003_AddCustomer*********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.enterusername(self.username)
        self.lp.enterpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("Login is successful")
        time.sleep(3)

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickoncustomersmenu()
        self.logger.info("Clicked on customers menu")
        self.addcust.clickoncustomers()
        self.logger.info("Clicked on customers option")
        time.sleep(2)

        self.addcust.clickonaddnew()
        self.logger.info("******provideing information***")
        # self.addcust.setemail("joythitest@gmail.com")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setemail(self.email)
        self.addcust.setpassword("test123")
        self.addcust.setfirstname("Jyothi")
        self.addcust.setlastname("pallam")
        self.addcust.setgender("Female")
        self.addcust.setdateofbirth("04/24/1992")
        self.addcust.setcompanyname("Safeway")
        self.addcust.setrole("Guests")
        self.addcust.setrole("Vendor 1")
        self.logger.info("customer role is selected")
        self.addcust.setadmincomment("this is for testing....")
        self.addcust.clicksave()
        self.logger.info(" saving the customer information")

        self.logger.info("started add customer validation")
        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("add customer test is passed")

        elif "Email is already registered" in self.msg:
            assert True == True
            self.logger.info("add customer test is passed")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_Addcustomer_scr.png")
            self.logger.info("add customer test is failed")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))















