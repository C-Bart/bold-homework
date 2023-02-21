from locators.login_locator import LoginLocator
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://app.interviewme.pl/login"
        self.locators = LoginLocator()

    def open(self):
        self.driver.get(self.url)
        self.load_page()

    def fill_input_email(self, login):
        self.driver.find_element(*self.locators.INPUT_EMAIL).send_keys(login)

    def fill_input_password(self, password):
        self.driver.find_element(*self.locators.INPUT_PASSWORD).send_keys(password)

    def submit_login(self):
        self.driver.find_element(*self.locators.SUBMIT_BUTTON_LOGIN).click()
