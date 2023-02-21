import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service("./chromedriver.exe"))
    yield driver
    driver.close()
