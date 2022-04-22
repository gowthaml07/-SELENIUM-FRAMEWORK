import os
from datetime import datetime

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.chrome.service import Service



@pytest.fixture()
def setup():
    service_object = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_object)
    return driver

# ========================  Report ============================
project_file = os.path.abspath(os.path.join(__file__,'..','..'))
report_file = os.path.join(project_file,'Reports')

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.join(report_file,'reports-'+datetime.now().strftime("%d-%m--%H-%M")+'.html')