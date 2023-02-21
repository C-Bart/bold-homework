from selenium.webdriver.common.by import By


class LoginLocator:

    INPUT_EMAIL = (By.XPATH, "//input[@name='email']")
    INPUT_PASSWORD = (By.XPATH, "//input[@name='password']")

    SUBMIT_BUTTON_LOGIN = (By.XPATH, "//button[@data-test='auth-login-submit']")
