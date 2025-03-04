from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    LOCATOR_PASS_FIELD = (By.XPATH, '''//*[@id="login"]/div[2]/label/input''')
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_LOGIN_ENTER = (By.XPATH,"""//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CREATE_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/button')
    LOCATOR_CREATE_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_CREATE_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CREATE_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_CREATE_POST_BTN = (By.XPATH, '//*[@id="create-item"]/div/div/div[7]/div/button')
    LOCATOR_RES_CREATE = (By.XPATH, """//*[@id="app"]/main/div/div[3]/div[1]/a/h2""")
    LOCATOR_HOME = (By.XPATH, """//*[@id="app"]/main/nav/a/span""")
    LOCATOR_CONTACT = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]""")
    LOCATOR_YOUR_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_YOUR_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_YOUR_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")
class OperationsHelper(BasePage):

    def enter_login(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}')
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        logging.info('Click login button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f'We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return text

    def get_login_enter_text(self):
        enter_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_ENTER, time=2)
        text = enter_field.text
        logging.info(f'We find text {text} in error field {TestSearchLocators.LOCATOR_LOGIN_ENTER[1]}')
        return text

    def click_create_button(self):
        logging.info('Click create post button')
        self.find_element(TestSearchLocators.LOCATOR_CREATE_BUTTON).click()

    def create_post_title(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_CREATE_TITLE[1]}')
        title_field = self.find_element(TestSearchLocators.LOCATOR_CREATE_TITLE)
        title_field.clear()
        title_field.send_keys(word)

    def create_post_description(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_CREATE_DESCRIPTION[1]}')
        description_field = self.find_element(TestSearchLocators.LOCATOR_CREATE_DESCRIPTION)
        description_field.clear()
        description_field.send_keys(word)

    def create_post_content(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_CREATE_CONTENT[1]}')
        content_field = self.find_element(TestSearchLocators.LOCATOR_CREATE_CONTENT)
        content_field.clear()
        content_field.send_keys(word)

    def click_create_post_button(self):
        logging.info('Click create post button')
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()

    def get_res_create_text(self):
        enter_field = self.find_element(TestSearchLocators.LOCATOR_RES_CREATE, time=2)
        text = enter_field.text
        logging.info(f'We find text {text} in error field {TestSearchLocators.LOCATOR_RES_CREATE[1]}')
        return text

    def click_contact(self):
        logging.info('Click contact button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT).click()

    def contact_us_name(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_YOUR_NAME[1]}')
        title_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_NAME)
        title_field.clear()
        title_field.send_keys(word)

    def contact_us_email(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_YOUR_EMAIL[1]}')
        title_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_EMAIL)
        title_field.clear()
        title_field.send_keys(word)

    def contact_us_content(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_YOUR_CONTENT[1]}')
        title_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_CONTENT)
        title_field.clear()
        title_field.send_keys(word)

    def click_contact_us(self):
        logging.info('Click create contact button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def alert(self):
        alert = self.driver.switch_to.alert
        return alert.text