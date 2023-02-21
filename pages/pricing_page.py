from selenium.webdriver.support import expected_conditions as EC

from locators.pricing_locator import PricingLocator
from pages.base_page import BasePage


class PricingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = PricingLocator

    def select_14_days_pricing(self):
        self.driver.find_element(*self.locator.PLAN_14_DAYS).click()

    def proceed_pricing(self):
        self.wait.until(EC.visibility_of_element_located(self.locator.BUTTON_PROCEED_PRICING))
        button = self.driver.find_element(*self.locator.BUTTON_PROCEED_PRICING)
        self.wait.until(EC.element_to_be_clickable(button))
        button.click()
