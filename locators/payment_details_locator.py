from selenium.webdriver.common.by import By


class PaymentDetailsLocator:

    BUTTON_PAYMENT_CONFIRMATION = (By.XPATH, "//button[@data-test='cart-pay-securely']")
    BUTTON_PAYMENT_CONFIRMATION_LOADER = (By.XPATH, "//*[name()='svg']//*[name()='circle']")

    IFRAME_PAYMENT = (By.XPATH, "//iframe[@id='ccframe']")

    INPUT_CARD_NUMBER = (By.XPATH, "//input[@id='ccNum']")
    INPUT_CARD_EXPIRATION = (By.XPATH, "//input[@name='expirationDate']")
    INPUT_CARD_CVV = (By.XPATH, "//input[@id='ccCVV']")
    INPUT_CARD_HOLDER_NAME = (By.XPATH, "//input[@name='cardholderName']")

    HEADER_WITH_TEXT = (By.XPATH, "//h3[text()='{}']")
    LINK = (By.XPATH, "//a[@href='{}']")
