from selenium.webdriver.common.by import By


class BaseLocator:

    LOADER = (By.XPATH, "//div[@id='init-loader']")
