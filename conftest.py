import pytest

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('testdata.yaml') as f:
    test_data = yaml.safe_load(f)
    browser = test_data['browser']


@pytest.fixture(scope='session')
def browser():
    if browser == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def title_name():
    return 'Hello'
@pytest.fixture()
def description_name():
    return 'world'
@pytest.fixture()
def content_name():
    return 'Hello world!'

@pytest.fixture()
def your_name():
    return 'Vasya'
@pytest.fixture()
def your_email():
    return 'Vasya@gmail.com'
@pytest.fixture()
def your_content():
    return 'Hello world!'