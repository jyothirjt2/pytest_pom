from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchCustomer:

    btnsearch_xpath = '//div[@class="search-text"]'
    txtsrchemail_xpath = '//*[@id="SearchEmail"]'
    txtfrstname_xpath = '//*[@id="SearchFirstName"]'
    txtlstname_xpath = '//*[@id="SearchLastName"]'
    btnsearchcustomer_xpath = '//*[@id="search-customers"]'

    table_xpath = '//table[@id="customers-grid"]'
    table_rows_xpath = '//table[@id="customers-grid"]//tbody/tr'
    table_columns_xpath = '//table[@id="customers-grid"]//tbody/tr/td'

    def __init__(self,driver):
        self.driver = driver

    def clickOnsearchbtn(self):
        self.driver.find_element(By.XPATH, self.btnsearch_xpath).click()
    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtsrchemail_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtsrchemail_xpath).send_keys(email)
    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH, self.txtfrstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtfrstname_xpath).send_keys(firstname)
    def Clicksearch(self):
        self.driver.find_element(By.XPATH, self.btnsearch_xpath).click()
    def getRowCount(self):
        return len(self.driver.find_elements(By.XPATH, self.table_rows_xpath))
    def getColumnCount(self):
        return len(self.driver.find_elements(By.XPATH, self.table_columns_xpath))
    def searchCustByEmail(self,email):
        flag=False
        for r in range(1,self.getRowCount()+1):
            table = self.driver.find_element(By.XPATH,self.table_xpath)
            emailid = table.find_element(By.XPATH, '//table[@id="customers-grid"]//tbody/tr["+str(r)+"]/td[2]').text
            if emailid == email:
                flag = True
                break
        return flag
    def searchCustbyName(self,Name):
        string_name_xpath = '//table[@id="customers-grid"]/tbody/tr["+str+"]/td[3]'
        flag = False
        for r in range(1, self.getColumnCount()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, self.string_name_xpath).text
            if name == Name:
                flage = True
                break
        return flag
    













