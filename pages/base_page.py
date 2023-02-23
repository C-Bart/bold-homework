
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.base_locator import BaseLocator


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_locator = BaseLocator()

    def load_page(self):
        self.wait.until(EC.invisibility_of_element(self.base_locator.LOADER))

    def accept_cookies(self):
        element = self.base_locator.ACCEPT_COOKIES
        self.wait.until(EC.element_to_be_clickable(element))
        self.driver.find_element(*element).click()

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url(self, url):
        self.wait.until(lambda driver: driver.current_url == url)
