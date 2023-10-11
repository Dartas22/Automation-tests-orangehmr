from playwright.sync_api import Page, sync_playwright
from time import sleep
import sys
sys.path.append('D:\\VC\\testing_proj\\tests\\features\\steps')
from auxiliary_functions import remove_spaces

import pyperclip
from pytest_bdd import scenario, given, when, then, parsers
from time import sleep


name_check_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/p[1]'

sys.path.append('D:\\VC\\testing_proj\\tests\\features')
@scenario('..\\..\\directory_subpage.feature', 'Find employee by name')
def test_directory_search_by_name():
    pass

@given(u'Opem Orange HRM on Directory page')
def open_buzz_page(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/directory/viewDirectory")
    

@given(parsers.parse(u'Login to Orange HRM with "{user}" and "{password}"'))
def login(page: Page):
    page.get_by_placeholder("Username").fill('admin')
    page.get_by_placeholder("Password").fill('admin123')
    page.locator('button[type="submit"]:has-text("Login")').click()

@when(parsers.parse(u'Type "{employee}" in Employee Name and select first one'))
def emp_input(page: Page, employee):
    page.get_by_placeholder('Type for hints...').fill(employee)
    sleep(2.5)
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")

@when(u'Get name of selected employee')
def get_emp_name(page: Page):
    global name

    page.keyboard.down("Shift")
    for i in range(40):
        page.keyboard.press("ArrowLeft")
    page.keyboard.up("Shift")
    sleep(1.5)
    page.keyboard.press('Control+C')
    name = remove_spaces(pyperclip.paste())


@when(u'Click Search button')
def click_search(page: Page):
    page.locator('button[type="submit"]:has-text("Search")').click()
    sleep(0.5)

@then(u'Check if employee with proper name appeared')
def check_if_proper_emp_appeared(page: Page):
    name_check = page.locator(name_check_xpath).inner_text()
    name_check = remove_spaces(name_check)

    assert name == name_check