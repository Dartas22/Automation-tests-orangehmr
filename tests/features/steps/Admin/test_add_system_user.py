from playwright.sync_api import Page, sync_playwright
from time import sleep
import sys

from pytest_bdd import scenario, given, when, then, parsers
from time import sleep


records_count_xp = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span'
delete_button_xp = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[6]/div/button[1]'
confirm_delete_button_xp = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'
displayed_username_xp = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div'

sys.path.append('D:\\VC\\testing_proj\\tests\\features')
@scenario('..\\..\\admin_subpage.feature', 'Add system user')
def test_admin_add_system_user():
    pass

@given(u'Opem Orange HRM on Admin page')
def open_admin_page(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    

@given(parsers.parse(u'Login to Orange HRM with "{user}" and "{password}"'))
def login(page: Page, user, password):
    page.get_by_placeholder("Username").fill(user)
    page.get_by_placeholder("Password").fill(password)
    page.locator('button[type="submit"]:has-text("Login")').click()

@when(parsers.parse(u'Check if "{username}" exist and delete it'))
def select_employee(page: Page, username):
    page.get_by_role("textbox").nth(1).fill(username)
    page.get_by_role("button", name="Search").click()
    sleep(3)
    if page.locator(records_count_xp).inner_text() != 'No Records Found':
        page.locator(delete_button_xp).click()
        sleep(0.5)
        page.locator(confirm_delete_button_xp).click()
        sleep(0.5)

@when(u'Click +Add button')
def click_add_button(page: Page):
    page.locator('button[type="button"]:has-text("Add")').click()

@when(u'Click on User Role field and select admin')
def select_role(page: Page):
    page.get_by_text("-- Select --").first.click()
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")

@when(parsers.parse(u'Type "{employee}" in Employee Name and select first one'))
def select_employee(page: Page, employee):
    page.get_by_placeholder('Type for hints...').fill(employee)
    sleep(2.5)
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")

@when(u'Select Enabled status')
def select_status(page: Page):
    page.locator("form i").nth(1).click()
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")

@when(parsers.parse(u'Enter Username "{username}"'))
def set_username(page: Page, username):
    page.get_by_role("textbox").nth(2).fill(username)

@when(parsers.parse(u'Type Password "{password}" and confirm it'))
def set_password(page: Page, password):
    page.get_by_role("textbox").nth(3).fill(password)
    page.get_by_role("textbox").nth(4).fill(password)

@when(u'Click Save button')
def click_save_button(page: Page):
    page.get_by_role("button", name="Save").click()
    sleep(1.5)

@then(parsers.parse(u'Search for user "{username}"'))
def search_for_user(page: Page, username):
    page.get_by_text("-- Select --").first.click()
    page.get_by_role("textbox").nth(1).fill(username)
    sleep(1)
    page.get_by_role("button", name="Search").click()
    sleep(1)

@then(parsers.parse(u'Confirm that "{username}" appears'))
def confirm_that_user_appears(page: Page, username):
    username_confirm = page.locator(displayed_username_xp).inner_text()

    assert username_confirm == username