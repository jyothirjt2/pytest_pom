from selenium import webdriver
from selenium.webdriver.common.by import By
import random

class AddCustomer:

    lnk_dashboard_xpath = '//*[@id="nopSideBarPusher"]'
    link_customersmenu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_customers_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    button_addnew_xpath = '//a[@href="/Admin/Customer/Create"]'

    textfiled_email_xpath = '//input[@id="Email"]'
    textfiled_password_xpath = '//*[@id="Password"]'
    textfiled_firstname_xpath = '//*[@id="FirstName"]'
    textfiled_lastname_xpath = '//*[@id="LastName"]'
    btn_malegender_id = "Gender_Male"
    btn_femalegender_id= "Gender_Female"
    txtfield_dob_xpath = '//*[@id="DateOfBirth"]'

    txtfield_companyname_xpath = '//*[@id="Company"]'
    listtxtbx_role_xpath = '//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div'
    list_aministration_xpath = '//li[contains(text(), "Administrators")]'
    list_guests_xpath ='//li[contains(text(), "Guests")]'
    list_registered_xpath = '//li[contains(text(), "Registered")]'
    list_vendor_xpath =  '//li[contains(text(), "Vendors")]'
    drpdn_vendormngr_xpath = '//*[@id="VendorId"]'
    txtfield_admincomment_xpath = '//*[@id="AdminComment"]'
    btn_save_xpath = '//button[@name="save"]'

    def __init__(self,driver):
        self.driver = driver

    def clickondashbord(self):
        self.driver.find_element(By.XPATH,self.lnk_dashboard_xpath).click()
    def clickoncustomersmenu(self):
        self.driver.find_element(By.XPATH,self.link_customersmenu_xpath).click()
    def clickoncustomers(self):
        self.driver.find_element(By.XPATH,self.lnk_customers_xpath).click()
    def clickonaddnew(self):
        self.driver.find_element(By.XPATH,self.button_addnew_xpath).click()
    def setemail(self,mailid):
        self.driver.find_element(By.XPATH,self.textfiled_email_xpath).send_keys(mailid)
    def setpassword(self,password):
        self.driver.find_element(By.XPATH,self.textfiled_password_xpath).send_keys(password)
    def setfirstname(self,firstname):
        self.driver.find_element(By.XPATH,self.textfiled_firstname_xpath).send_keys(firstname)
    def setlastname(self,lastname):
        self.driver.find_element(By.XPATH,self.textfiled_lastname_xpath).send_keys(lastname)
    def setgender(self,gender):
        if gender == 'Male':
            self.driver.find_element(By.ID,self.btn_malegender_id).send_keys(gender)
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.btn_femalegender_id).send_keys(gender)
        else:
            elf.driver.find_element(By.ID, self.btn_femalegender_id).send_keys(gender)
    def setdateofbirth(self,dateofbirth):
        self.driver.find_element(By.XPATH,self.txtfield_dob_xpath).send_keys(dateofbirth)
    def setcompanyname(self,companyname):
        self.driver.find_element(By.XPATH,self.txtfield_companyname_xpath).send_keys(companyname)
    def setrole(self,role):
        # self.driver.find_element(By.XPATH, self.listtxtbx_role_xpath).clear()
        self.driver.find_element(By.XPATH,self.listtxtbx_role_xpath).click()
        time.sleep(2)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.list_registered_xpath)
        elif role == 'Aministration':
            self.listitem = self.driver.find_element(By.XPATH, self.list_aministration_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH,self.list_guests_xpath)
        time.sleep(2)
        # self.listitem.click()  to click the listitems      python code
        self.driver.execute_script("arguments[0].click();",self.listitem)         #when click is not wrking we can use this java script method
    def setvendormanager(self,value):
        dropdwn = Select(self.driver.find_element(By.XPATH,self.drpdn_vendormngr_xpath))
        dropdwn.select_by_visible_text(value)

    def setadmincomment(self,comment):
        self.driver.find_element(By.XPATH,self.txtfield_admincomment_xpath).sendkeys(comment)
    def clicksave(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()






















