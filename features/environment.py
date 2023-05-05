from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


def browser_init(context, test_name):
    """
    :param context: Behave context
    """
    # service = Service('C:/User/soxano/Documents/Automation/python-selenium-automation/chromedriver.exe')
    # context.driver = webdriver.Chrome(service=service)


    # # Firefox
    # options = Options()
    # options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'
    # context.driver = webdriver.Firefox(options=options, executable_path=r'C:/Users/oxano/Documents/Internship/cureskin/geckodriver.exe')
    # # # Firefox


       #Mobile
    # mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # context.driver = webdriver.Chrome(options=chrome_options)
    #

    ## HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     service=service
    # )


    ## HEADLESS MODE Firefox ####
    options = Options()
    options.headless = True
    options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'
    context.driver = webdriver.Firefox(options=options, executable_path=r'C:/Users/oxano/Documents/Internship/cureskin/geckodriver.exe')


    # for browerstack ###

    # desired_cap = {
    #     'browserName': 'Firefox',
    #     'bstack:options': {
    #         'os': 'Windows',
    #         'osVersion': '10',
    #         'sessionName': test_name
    #     }
    # }
    # bs_user = 'oksana_iPLW6X'
    # bs_key = 'WKjsVGNJ3GGmpQqcsKUy'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
