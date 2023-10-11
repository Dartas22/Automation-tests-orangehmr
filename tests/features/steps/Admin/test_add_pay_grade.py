from playwright.sync_api import Page, sync_playwright
from time import sleep
import sys
sys.path.append('D:\\VC\\testing_proj\\tests\\features\\steps')
from auxiliary_functions import return_result_number

import pyperclip
from pytest_bdd import scenario, given, when, then, parsers
from time import sleep

records = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[2]/div/span'
name_1 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div['
name_2 = ']/div/div[2]/div'

sys.path.append('D:\\VC\\testing_proj\\tests\\features')
@scenario('..\\..\\admin_subpage.feature', 'Add pay grade')
def test_admin_add_pay_grade():
    pass

@given(u'Opem Orange HRM on Admin page')
def open_buzz_page(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    

@given(parsers.parse(u'Login to Orange HRM with "{user}" and "{password}"'))
def login(page: Page, user, password):
    page.get_by_placeholder("Username").fill(user)
    page.get_by_placeholder("Password").fill(password)
    page.locator('button[type="submit"]:has-text("Login")').click()

@when(u'Click on job and select pay grade')
def select_pay_grade(page: Page):
    page.get_by_text("Job").click()
    page.get_by_text("Pay Grades").click()
    sleep(1)

@when(parsers.parse(u'If "{name}" and "{currency}" exist delete record'))
def remove_record(page: Page, name, currency):
    if page.get_by_text(name).is_visible():
        page.get_by_role("row", name=f" {name} {currency}  ").get_by_role("button").first.click()
        page.get_by_role("button", name=" Yes, Delete").click()


@when(u'Click add button')
def click_add_button(page: Page):
    page.get_by_text("Add").click()

@when(parsers.parse(u'Set "{name}" and click save button'))
def set_name(page: Page, name):
    sleep(1)
    page.get_by_role("textbox").nth(1).fill(name)
    page.get_by_text("Save").click()

@when(parsers.parse(u'Click add button and select "{currency}"'))
def select_currency(page: Page, currency):
    page.get_by_role("button", name=" Add").click()
    page.get_by_text("-- Select --").click()
    page.get_by_role("option", name="PLN - Polish Zloty").click()

@when(parsers.parse(u'Set "{minimum}" and "{maximum}" salary and click save button'))
def set_salary(page: Page, minimum, maximum):
    page.get_by_role("textbox").nth(2).fill(minimum)
    page.get_by_role("textbox").nth(3).fill(maximum)
    page.get_by_role("button", name="Save").nth(1).click()

@then(u'Return to pay grade page')
def return_to_pay_grade(page: Page):
    page.get_by_text("Job").click()
    page.get_by_text("Pay Grades").click()

@then(parsers.parse(u'Check if "{name}" whit proper "{currency}" occurs'))
def set_salary(page: Page, name, currency):
    sleep(1)
    rows = return_result_number(page.locator(records).inner_text())
    result_row = None
    for i in range(1, rows+1):
        row = name_1 + str(i) + name_2
        if page.locator(row).inner_text() == name:
            result_row = i
            break

    found_currency = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[' + str(result_row) + ']/div/div[3]/div'
    
    assert page.locator(row).inner_text() == name and page.locator(found_currency).inner_text() == currency