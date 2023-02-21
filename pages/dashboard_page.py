from selenium.webdriver.support import expected_conditions as EC

from locators.dashboard_locator import DashboardLocator
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = DashboardLocator()

    def load_page(self):
        super().load_page()
        self.wait.until(EC.visibility_of_element_located(self.locator.BUTTON_ADD_RESUME))

    def download_resume(self):
        self.wait.until(EC.visibility_of_element_located(self.locator.BUTTON_DOWNLOAD_RESUME))
        button = self.driver.find_element(*self.locator.BUTTON_DOWNLOAD_RESUME)
        self.wait.until(EC.element_to_be_clickable(button))
        button.click()

    def is_document_present(self, document):
        element = self.driver.find_element(self.locator.DOCUMENT[0], self.locator.DOCUMENT[1].format(document))
        return element.is_displayed()
