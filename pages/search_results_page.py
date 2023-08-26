from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class GoogleSearchResultsPage:
    def __init__(self, driver):
        self.driver = driver

    def suggested_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'a.gL9Hy')

    def first_result_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#rso > div:nth-child(4) > div > div > '
                                                         'div.kb0PBd.cvP2Ce.jGGQ5e > div > div > a > h3')

    def images_filter(self, filter_name):
        return self.driver.find_element(By.XPATH, f"//span[@class='FMKtTb UqcIvb' and text()='{filter_name}']")

    def current_filter(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'span[aria-current="page"]')
