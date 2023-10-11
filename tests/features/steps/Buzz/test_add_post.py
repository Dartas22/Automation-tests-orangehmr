from playwright.sync_api import Page, sync_playwright
from time import sleep
import pytest

from pytest_bdd import scenario, given, when, then, parsers
from time import sleep
import sys
sys.path.append('D:\\VC\\testing_proj\\tests\\features')


post_xp = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/p[1]'

@scenario('..\\..\\buzz_subpage.feature', 'Add post')
def test_add_post():
    pass

@given(u'Opem Orange HRM on Buzz page')
def open_buzz_page(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz")
    

@given(parsers.parse(u'Login to Orange HRM with "{user}" and "{password}"'))
def login(page: Page, user, password):
    page.get_by_placeholder("Username").fill(user)
    page.get_by_placeholder("Password").fill(password)
    page.locator('button[type="submit"]:has-text("Login")').click()

@when(parsers.parse(u'Put message "{message}"'))
def put_message(page: Page, message):
    page.locator('.oxd-buzz-post-input').fill(message)

@when(u'Click Post button')
def click_post(page: Page):
    page.locator('button.oxd-button--main:has-text("Post")').click()

@then(parsers.parse(u'Check if massage "{message}" appeared'))
def check_message(page: Page, message):
    new_post = page.locator(post_xp)
    assert new_post.text_content() == message
    page.context.close()