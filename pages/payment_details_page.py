from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from locators.payment_details_locator import PaymentDetailsLocator
from pages.base_page import BasePage


class PaymentDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = PaymentDetailsLocator()

    def load_page(self):
        self.wait.until(EC.visibility_of_element_located(self.locator.BUTTON_PAYMENT_CONFIRMATION))
        super().load_page()

    def fill_card_number(self, number):
        self.driver.switch_to.frame(self.get_payment_iframe())
        self.driver.find_element(*self.locator.INPUT_CARD_NUMBER).send_keys(number)
        self.driver.switch_to.default_content()

    def fill_card_expiration_date(self, date):
        self.driver.find_element(*self.locator.INPUT_CARD_EXPIRATION).send_keys(date)

    def fill_card_cvv(self, cvv):
        self.driver.switch_to.frame(self.get_payment_iframe())
        self.driver.find_element(*self.locator.INPUT_CARD_CVV).send_keys(cvv)
        self.driver.switch_to.default_content()

    def fill_card_holder_name(self, name):
        element = self.driver.find_element(*self.locator.INPUT_CARD_HOLDER_NAME)
        element.send_keys(Keys.COMMAND, "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(name)

    def get_payment_iframe(self):
        return self.driver.find_element(*self.locator.IFRAME_PAYMENT)

    def is_header_with_text_displayed(self, text):
        return self.driver.find_element(
            self.locator.HEADER_WITH_TEXT[0], self.locator.HEADER_WITH_TEXT[1].format(text)).is_displayed()

    def is_link_displayed(self, link):
        return self.driver.find_element(self.locator.LINK[0], self.locator.LINK[1].format(link)).is_displayed()

    def click_payment_button(self):
        self.wait.until(EC.element_to_be_clickable(self.locator.BUTTON_PAYMENT_CONFIRMATION))
        element = self.driver.find_element(*self.locator.BUTTON_PAYMENT_CONFIRMATION)
        element.click()
        # Fragment kodu poniżej jest raczej obejściem problemu opóźnionej walidacji pola dla kodu CVV.
        # W pierwszej kolejności szukałbym tutaj raczej możliwości poprawy po stronie aplikacji.
        try:
            self.wait.until(EC.visibility_of_element_located(self.locator.BUTTON_PAYMENT_CONFIRMATION_LOADER))
        except TimeoutException:
            element.click()


