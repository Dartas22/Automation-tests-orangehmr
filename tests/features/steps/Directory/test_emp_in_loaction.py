from playwright.sync_api import Page, sync_playwright
from time import sleep
import sys
sys.path.append('D:\\VC\\testing_proj\\tests\\features\\steps')
from auxiliary_functions import return_result_number

from pytest_bdd import scenario, given, when, then, parsers
from time import sleep


results_amount_xp = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/span'
emp_num_class = '.oxd-sheet.oxd-sheet--rounded.oxd-sheet--white.orangehrm-directory-card'


sys.path.append('D:\\VC\\testing_proj\\tests\\features')
@scenario('..\\..\\directory_subpage.feature', 'Check number of employees by location')
def test_directory_search_by_name():
    pass

@given(u'Opem Orange HRM on Directory page')
def open_buzz_page(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/directory/viewDirectory")
    

@given(parsers.parse(u'Login to Orange HRM with "{user}" and "{password}"'))
def login(page: Page, user, password):
    page.get_by_placeholder("Username").fill(user)
    page.get_by_placeholder("Password").fill(password)
    page.locator('button[type="submit"]:has-text("Login")').click()

@when(parsers.parse(u'Select Location and choose "{number}" position'))
def select_location(page: Page, number):
    page.locator("form i").nth(1).click()
    for i in range(int(number)):
        page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")

@when(u'Click search button')
def click_search(page: Page):
    sleep(1)
    page.get_by_role("button", name="Search").click()
    sleep(1)

@when(u'Check how many results there are')
def results_number_check(page: Page):
    global results_number

    results_number = page.locator(results_amount_xp).inner_text()
    results_number = return_result_number(results_number)

@then(u'Check if right amount of employees displays')
def check_amount(page: Page):
    sleep(2)
    emp_num = page.locator(emp_num_class).count()

    assert emp_num == results_number