import pytest
from selenium import webdriver
from PageObjects.Login_page import login
from webdriver_manager.chrome import ChromeDriverManager

class test_01_Login():
    baseURL = 'https://admin-demo.nopcommerce.com/'
    username = 'admin@yourstore.com'
    password = 'admin'

    def test_homepage(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title =='Your store. Login':
            assert True
        else:
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.li = login(self.driver)
        self.li.username_id(self.username)
        self.li.password_id(self.password)
        self.li.clickLogin()
        act_titel = self.driver.title
        self.driver.close()
        if act_titel =='Dashboard / nopCommerce administration':
            assert True
        else:
            assert False
