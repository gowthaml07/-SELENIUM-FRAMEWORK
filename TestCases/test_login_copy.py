import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver_initialise():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://admin-demo.nopcommerce.com/')
    driver.maximize_window()
    time.sleep(2)
    yield driver
    time.sleep(3)
    driver.close()

def test_enter_name(driver_initialise):
    username= driver_initialise.find_element(By.ID,'Email')
    username.clear()
    time.sleep(2)
    username.send_keys('admin@yourstore.com')
    password= driver_initialise.find_element(By.ID,'Password')
    password.clear()
    time.sleep(2)
    password.send_keys('admin')
    login_click = driver_initialise.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button')
    login_click.click()
    time.sleep(2)
    logout_click = driver_initialise.find_element(By.XPATH,'/html/body/div[3]/nav/div/ul/li[3]/a')
    logout_click.click()
    time.sleep(5)

