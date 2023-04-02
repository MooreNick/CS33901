from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

from behave import given, when, then, step

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

@given(u'I have navigated to {site}')
def stepOne(context, site):
    context.site = site
    context.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if not site.startswith("http"):
        site = "https://" + site
    context.browser.get(site)
    time.sleep(1)

@when(u'I search for {game}')
def stepTwo(context, game):
    element_id = "searchRedesignTemplateInput"
    search_input = context.browser.find_element(By.ID, element_id)
    search_input.clear() # clear placeholder text in search bar
    search_input.send_keys(game) # send searched game text
    search_input.send_keys(Keys.RETURN) # press enter
    time.sleep(2) # dont close the window
    

@then(u'I find items related to "{result}"')
def stepThree(context, result):
    page = context.browser.page_source
    assert result.upper() in page.upper()
