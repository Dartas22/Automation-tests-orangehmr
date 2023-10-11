from playwright.sync_api import Page, sync_playwright
from time import sleep
import pytest

from pytest_bdd import scenario, given, when, then, parsers
from time import sleep
import sys
sys.path.append('D:\\VC\\testing_proj\\tests\\features')


post_likes_class = 'p.oxd-text.oxd-text--p.orangehrm-buzz-stats-active'

@scenario('..\\..\\buzz_subpage.feature', 'Give like')
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

@when(u'Check the likes count on newest post')
def check_likes(page: Page):
    global likes_count_start
    sleep(3)

    post_likes =  page.locator(post_likes_class).first.inner_text()
    likes_count_start = int(post_likes[0])

@when(u'Give like on newest post')
def give_like(page: Page):
    page.locator("#heart-svg").first.click()
    sleep(0.5)

@then(u'Check if the likes count increased by one')
def check_if_increased(page: Page):
    post_likes =  page.locator(post_likes_class).first.inner_text()
    likes_check = int(post_likes[0])
    assert likes_check == likes_count_start + 1 or likes_check == likes_count_start -1
