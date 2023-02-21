from selenium.webdriver.common.by import By


class PricingLocator:

    BUTTON_PROCEED_PRICING = (By.XPATH, "//button[@data-test='cart-plan-continue']")

    PLAN_14_DAYS = (By.XPATH, "//dev[@data-test-id='15176']")
    PLAN_QUARTER = (By.XPATH, "//dev[@data-test-id='13472']")
