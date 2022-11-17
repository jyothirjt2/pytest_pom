import time
import pytest
import openpyexcel
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pageObjects.Loginpage import LoginPage
from Utilities.readproperties import ReadConfig
from Utilities.customlogger import LogGen
from Utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getapplicationURL()
    path = ".\\Testdata/DataDrivenLogin.xlsx"
    logger = LogGen.loggen()
    def test_login_ddt(self,setup):
        self.logger.info("Test_002_DDT_Login")
        self.logger.info("verifying test_login_ddt")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path,"Sheet1")
        print("num of rows in EXcel:",self.rows)

        list_status=[]

        for row in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,"Sheet1",row,1)
            self.password = XLUtils.readData(self.path,"Sheet1",row,2)
            self.exp = XLUtils.readData(self.path,"Sheet1",row,3)

            self.lp.enterusername(self.user)
            self.lp.enterpassword(self.password)
            self.lp.clicklogin()
            time.sleep(4)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("passed")
                    self.lp.clicklogout();
                    list_status.append("pass")
                elif self.exp != "pass":
                    self.logger.info("failed")
                    self.lp.clicklogout();
                    list_status.append("fail")
            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info("fail")
                    list_status.append("fail")
                elif self.exp == "fail":
                    self.logger.info("passed")
                    list_status.append("pass")


        if "fail" not in list_status:
            self.logger.info("Login Data driven test is passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("login data driven test is failed")
            self.driver.close()
            assert True

        self.logger.info("Completed Test_002_DDT_Login successfully")

















