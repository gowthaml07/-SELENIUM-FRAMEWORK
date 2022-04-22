import time
import pytest
from selenium import webdriver
from PageObjects.Login_page import Login
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.readProperties import ReadConfig


class Test_01_Login:
    baseURL = ReadConfig.URL()
    username = ReadConfig.Login_username()
    password = ReadConfig.Login_password()



    def test_homepage(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title =='Your store. Login':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshorts" + "test_homepage.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.li = Login(self.driver)
        self.li.set_username(self.username)
        self.li.set_password(self.password)
        self.li.clickLogin()
        act_titel = self.driver.title
        self.driver.close()
        if act_titel == 'Dashboard / nopCommerce administration':
            assert True
        else:
            assert False
