from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open search results page')
def open_search_page(context):
    context.app.search_page.open_search_page()


@then('Verify first results have name, image, and price')
def verify_first_results_have_name_img_price(context):
    context.app.search_page.verify_first_results_have_name_img_price()
