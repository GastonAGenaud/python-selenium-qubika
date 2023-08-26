from selenium import webdriver


def initialize_driver():
    driver = webdriver.Chrome()
    return driver
