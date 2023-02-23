from selenium.webdriver.common.by import By


class BaseLocator:

    ACCEPT_COOKIES = (By.XPATH, "//button[@data-test='accept-cookies-button']")
    LOADER = (By.XPATH, "//div[@id='init-loader']")
