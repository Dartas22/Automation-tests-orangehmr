from playwright.sync_api import Page, sync_playwright
from time import sleep
import pytest

from pytest_bdd import scenario, given, when, then, parsers
from time import sleep
import sys
sys.path.append('D:\\VC\\testing_proj\\tests\\features')

share_main_page = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[3]/div[1]/button[2]'
share_message = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/p[1]'

@scenario('..\\..\\buzz_subpage.feature', 'Share post')
def test_share_post():
    pass

@given(u'Opem Orange HRM on Buzz page')
def open_buzz_page(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz")
    

@given(parsers.parse(u'Login to Orange HRM with "{user}" and "{password}"'))
def login(page: Page, user, password):
    page.get_by_placeholder("Username").fill(user)
    page.get_by_placeholder("Password").fill(password)
    page.locator('button[type="submit"]:has-text("Login")').click()

@when(u'Click share button below post')
def click_share_button_post(page: Page):
    page.locator(share_main_page).click()
    sleep(0.5)

@when(parsers.parse(u'Send message "{message}"'))
def send_message(page: Page, message):
    page.get_by_role("dialog").get_by_placeholder("What's on your mind?").fill(message)

@when(u'Click share button to publish')
def click_share_to_publish(page: Page):
    page.get_by_role("button", name="Share", exact=True).click()
    sleep(0.5)

@then(parsers.parse(u'Check if new post with "{message}" message appeared'))
def check_if_shared(page: Page, message):
    message_check = page.locator(share_message).inner_text()
    sleep(3)
    
    assert message_check == message