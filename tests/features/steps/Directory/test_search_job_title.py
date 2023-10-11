from playwright.sync_api import Page, sync_playwright
from time import sleep

from pytest_bdd import scenario, given, when, then, parsers
from time import sleep
import sys

'''Test have to be run in headed mode, beacause in headless it returns false failure'''

search_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
job_title_input_xp = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
emp_job_title_xp = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/p[2]'


sys.path.append('D:\\VC\\testing_proj\\tests\\features')
@scenario('..\\..\\directory_subpage.feature', 'Find emplyee by job title')
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

@when(u'Select Job Title and choose the first one')
def select_job_title(page: Page):
    page.locator(job_title_input_xp).click()
    page.keyboard.press('ArrowDown')
    page.keyboard.press('Enter')

@when(u'Get name of selected job')
def get_job_name(page: Page):
    global selected_job

    page.wait_for_selector(job_title_input_xp, timeout=2000)
    selected_job = page.locator(job_title_input_xp).inner_text()

@when(u'Click Search button')
def click_search_button(page: Page):
    page.locator(search_button).click()

@then(u'Check if first employee has proper job title')
def check_job_title(page: Page):
    page.wait_for_selector(emp_job_title_xp, timeout=2000)
    emp_job_title = page.locator(emp_job_title_xp).inner_text()

    assert emp_job_title == selected_job
