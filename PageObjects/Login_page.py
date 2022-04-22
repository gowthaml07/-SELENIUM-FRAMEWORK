import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Login:
    username_id = 'Email'
    password_id = 'Password'
    login_xpath = "//button[contains(text(),'Log in')]"
    logout_linktext = 'Logout'

    def __init__(self,driver):
        self.driver = driver

    def set_username(self,username):
        self.driver.find_element(By.ID,self.username_id).clear()
        self.driver.find_element(By.ID,self.username_id).send_keys(username)

    def set_password(self,passwaord):
        self.driver.find_element(By.ID,self.password_id).clear()
        self.driver.find_element(By.ID,self.password_id).send_keys(passwaord)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.login_xpath).click()


    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.logout_linktext).click()

