from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by_locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(by_locator)
        )
        return element