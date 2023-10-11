from playwright.sync_api import Page, sync_playwright
from time import sleep
import pytest

from pytest_bdd import scenario, given, when, then, parsers
from time import sleep
import sys
sys.path.append('D:\\VC\\testing_proj\\tests\\features')


show_more_less_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[4]/p'

@scenario('..\\..\\buzz_subpage.feature', 'Add comment')
def test_add_comment():
    pass

@given(u'Opem Orange HRM on Buzz page')
def open_buzz_page(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz")
    

@given(parsers.parse(u'Login to Orange HRM with "{user}" and "{password}"'))
def login(page: Page, user, password):
    page.get_by_placeholder("Username").fill(user)
    page.get_by_placeholder("Password").fill(password)
    page.locator('button[type="submit"]:has-text("Login")').click()

@when(u'Click the Comment button')
def click_comment_button(page: Page):
    page.locator(".orangehrm-buzz-post-actions > button").first.click()
    sleep(0.5)

@when(parsers.parse(u'Write message "{message}"'))
def write_message(page: Page, message):
    #comment_input.fill(message)
    page.get_by_placeholder("Write your comment...").first.fill(message)
    sleep(0.2)
    page.keyboard.press('Enter')
 
@when(u'If Show More button is visible click it')
def click_show_more(page: Page):
    show_more_button = page.locator(show_more_less_button)
    if show_more_button.is_visible():
        while show_more_button.inner_text() == "Show More":
            show_more_button.click()
            sleep(0.5)


@then(parsers.parse(u'Check if comment with "{message}" appeared'))
def check_comment(page: Page, message):
    comment_cout = 2
    comment = page.locator('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[4]/div[' + str(comment_cout) +']/div[2]/div[1]/span[1]')

    comment_exist = True
    while comment_exist:
        comment_cout += 1
        comment_exist = page.locator('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[4]/div[' + str(comment_cout) +']/div[2]/div[1]/span[1]').is_visible()

    comment_cout -= 1
    comment = page.locator('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[4]/div[' + str(comment_cout) +']/div[2]/div[1]/span[1]')    

    assert comment.inner_text() == message
