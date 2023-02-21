from selenium.webdriver.common.by import By


class DashboardLocator:

    BUTTON_ADD_RESUME = (By.XPATH, "//button[@data-test='dashboard-add-new-resume']")
    BUTTON_DOWNLOAD_RESUME = (By.XPATH, "//button//span[text()='Pobierz CV']")
    DOCUMENT = (By.XPATH, "//div[@data-info='user-admin-grid-column']//span[text()='{}']")
