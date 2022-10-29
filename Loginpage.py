from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_xpath = '//*[@id="Email"]'
    textbox_password_xpath = '//*[@id="Password"]'
    button_login_xpath = "//button[normalize-space()='Log in']"
    link_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver = driver

    def enterusername(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)
    def enterpassword(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)
    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()
    def clicklogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()







