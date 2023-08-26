from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from behave import *
from pages.search_results_page import GoogleSearchResultsPage
from pages.google_main_page import  GoogleHomePage
from support.driver_setup import initialize_driver


@given('I am on the Google homepage')
def step_impl(context):
    context.driver = initialize_driver()
    context.driver.get('https://www.google.com/')
    context.google_home_page = GoogleHomePage(context.driver)


@then('I should see the correct title, menu and search bar')
def step_impl(context):
    assert "Google" in context.driver.title
    assert context.google_home_page.menu()
    assert context.google_home_page.search_box()


@when('I search for "{text}"')
def step_impl(context, text):
    search_box = context.google_home_page.search_box()
    search_box.send_keys(text)
    search_box.send_keys(Keys.ENTER)
    context.google_search_results_page = GoogleSearchResultsPage(context.driver)


@then('I should see the suggestion "{suggestion}"')
def step_impl(context, suggestion):
    suggested_text = context.google_search_results_page.suggested_text().text
    assert suggestion.lower() in suggested_text.lower()


@when('I click on the suggestion "{suggestion}"')
def step_impl(context, suggestion):
    context.google_search_results_page.suggested_text().click()


@then('I should see the search results for "{text}"')
def step_impl(context, text):
    page_title = context.driver.title
    print('\n' + page_title)
    print(text.lower())
    assert text.lower() in page_title.lower()
    assert text.lower() in context.google_home_page.search_box().get_attribute('value').lower()
    first_result_title = context.google_search_results_page.first_result_title().text
    assert text.lower() in first_result_title.lower()


@when('I click on the "{filter_text}" filter')
def step_impl(context, filter_text):
    context.google_search_results_page.images_filter(filter_text).click()


@then('I should see the images results for "{text}" with the filter "{text_filter}"')
def step_impl(context, text, text_filter):
    current_filter = context.google_search_results_page.current_filter().text
    assert text_filter.lower() in current_filter.lower()