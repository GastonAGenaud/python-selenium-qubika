from selenium.webdriver.common.by import By


class GoogleHomePage:
    def __init__(self, driver):
        self.driver = driver

    def search_box(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'textarea[type="search"]')

    def menu(self):
        return self.driver.find_element(By.ID, 'gb')

    def page_title(self):
        return self.driver.find_element(By.XPATH, '//title')
