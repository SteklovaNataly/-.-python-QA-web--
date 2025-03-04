from testpage import OperationsHelper
import logging
import yaml
import time

with open('testdata.yaml') as f:
    test_data = yaml.safe_load(f)

def test_step_1(browser):
    logging.info("Test 1 Srarting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401'

def test_step_2(browser):
    logging.info("Test 2 Srarting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(test_data['login'])
    testpage.enter_pass(test_data['password'])
    testpage.click_login_button()
    assert testpage.get_login_enter_text() == 'Blog'

def test_step_3(browser, title_name, content_name, description_name):
    logging.info("Test 3 Srarting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(test_data['login'])
    testpage.enter_pass(test_data['password'])
    testpage.click_login_button()
    testpage.click_create_button()
    time.sleep(test_data['sleep_time'])
    testpage.create_post_title(title_name)
    testpage.create_post_description(description_name)
    testpage.create_post_content(content_name)
    time.sleep(test_data['sleep_time'])
    testpage.click_create_post_button()
    time.sleep(test_data['sleep_time'])
    testpage.go_to_site()
    assert testpage.get_res_create_text() == title_name


def test_step_4(browser, your_name, your_email, your_content):
    logging.info("Test 4 Srarting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(test_data['login'])
    testpage.enter_pass(test_data['password'])
    testpage.click_login_button()
    testpage.click_contact()
    time.sleep(test_data['sleep_time'])
    testpage.contact_us_name(your_name)
    testpage.contact_us_email(your_email)
    testpage.contact_us_content(your_content)
    testpage.click_contact_us()
    time.sleep(test_data['sleep_time'])
    assert testpage.alert() == 'Form successfully submitted'