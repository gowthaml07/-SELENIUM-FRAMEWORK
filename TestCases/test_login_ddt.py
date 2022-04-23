import time
import pytest
from selenium import webdriver
from PageObjects.Login_page import Login
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.readProperties import ReadConfig
from Utilities import XLUtils


class Test_02_DDT_Login:
    baseURL = ReadConfig.URL()
    path = ReadConfig.Excel_file_path()

    def test_login_ddt(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.li = Login(self.driver)
        self.rows = XLUtils.rowCount(self.path, 'Sheet1')
        lst_status = []
        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.li.set_username(self.user)
            self.li.set_password(self.password)
            self.li.clickLogin()

            act_titel = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'

            if act_titel == exp_title:
                if self.exp == 'Pass':
                    self.li.clickLogout()
                    lst_status.append('Pass')
                elif self.exp == 'Fail':
                    self.li.clickLogout()
                    lst_status.append('Fail')
            elif act_titel != exp_title:
                if self.exp == 'Pass':
                    lst_status.append('Fail')
                elif self.exp == 'Fail':
                    lst_status.append('Pass')

        if 'Fail' not in lst_status:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False
