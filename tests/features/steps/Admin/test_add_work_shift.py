from playwright.sync_api import Page, sync_playwright
from time import sleep
import sys
sys.path.append('D:\\VC\\testing_proj\\tests\\features\\steps')
from auxiliary_functions import shift_length

import pyperclip
from pytest_bdd import scenario, given, when, then, parsers
from time import sleep

sys.path.append('D:\\VC\\testing_proj\\tests\\features')
@scenario('..\\..\\admin_subpage.feature', 'Add work shift')
def test_admin_add_work_shift():
    pass

@given(u'Opem Orange HRM on Admin page')
def open_buzz_page(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    

@given(parsers.parse(u'Login to Orange HRM with "{user}" and "{password}"'))
def login(page: Page, user, password):
    page.get_by_placeholder("Username").fill(user)
    page.get_by_placeholder("Password").fill(password)
    page.locator('button[type="submit"]:has-text("Login")').click()

@when(u'Click on job and select work shift')
def select_work_shift(page: Page):
    page.get_by_text("Job").click()
    page.get_by_text("Work Shifts").click()

@when(parsers.parse(u'If "{shift_name}" from "{work_from}" to "{work_to}" exist delet it'))
def check_if_shift_exist(page: Page, shift_name, work_from, work_to):
    sleep(1)
    hours = shift_length(work_from, work_to)
    if page.get_by_role("row", name=f" {shift_name} {work_from} {work_to} {hours}  ").is_visible():
        page.get_by_role("row", name=f" {shift_name} {work_from} {work_to} {hours}  ").get_by_role("button").first.click()
        page.get_by_role("button", name=" Yes, Delete").click()

@when(u'Click add button')
def select_work_shift(page: Page):
    page.get_by_text("Add").click()

@when(parsers.parse(u'Set "{shift_name}"'))
def set_shift_name(page: Page, shift_name):
    page.get_by_role("textbox").nth(1).fill(shift_name)

@when(parsers.parse(u'Set "{work_from}" and "{work_to}"'))
def set_work_hours(page: Page, work_from, work_to):
    page.get_by_placeholder('hh:mm').first.fill(work_from)
    page.get_by_placeholder('hh:mm').nth(1).fill(work_to)

@when(parsers.parse(u'In assigned employess type "{name}", choose first one and click save button'))
def set_employee_name(page: Page, name):
    page.get_by_placeholder("Type for hints...").fill(name)
    sleep(2)
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")
    page.get_by_text("Save").click()

@then(parsers.parse(u'Check if "{shift_name}" from "{work_from}" to "{work_to}" appeares'))
def check_if_shift_appears(page: Page, shift_name, work_from, work_to):
    sleep(4)
    hours = shift_length(work_from, work_to)
    assert page.get_by_role("row", name=f" {shift_name} {work_from} {work_to} {hours}  ").is_visible()