import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.Loginpage import LoginPage
from pageObjects.addcustomerpage import AddCustomer
from pageObjects.searchcustomer_page import SearchCustomer
from Utilities.readproperties import ReadConfig
from Utilities.customlogger import LogGen


class Test_SearchCustByEmail_004:
    baseURL = ReadConfig.getapplicationURL()
    username = ReadConfig.getusername()
    password= ReadConfig.getpassword()
    logger =LogGen.loggen()

    def test_searchCustomer(self,setup):
        self.logger.info(" Test_004_addcustomer ")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp =LoginPage(self.driver)
        self.lp.enterusername(self.username)
        self.lp.enterpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("****Login Succesfull********")

        self.logger.info("******** Starting searching customer by email  *************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickoncustomersmenu()
        self.addcust.clickoncustomers()
        self.logger.info("******** started setting email on textfiled *************")
        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.searchbtn()
        time.sleep(2)
        self.searchcust.setEmail("steve_gates@nopCommerce.com")
        time.sleep(6)
        self.searchcust.clickcustsearch()
        self.searchcust.setFirstName("Steve Gates")
        self.logger.info("**** clicked on searchcustbutton****")
        self.logger.info("******** looking for search result *************")
        status = self.searchcust.searchCustByEmail("steve_gates@nopCommerce.com")
        time.sleep(3)
        assert True == status
        self.logger.info("****** Test_SearchCustByEmail_004 is Finished ")














