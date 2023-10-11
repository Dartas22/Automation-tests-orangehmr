from playwright.sync_api import Page, sync_playwright
from time import sleep
import sys

from pytest_bdd import scenario, given, when, then, parsers
from time import sleep


job_title_input_xp = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input'
results_count_xp = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[2]/div/span'

sys.path.append('D:\\VC\\testing_proj\\tests\\features')
@scenario('..\\..\\admin_subpage.feature', 'Add job title')
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

@when(u'Click on Job and select Job Titles')
def select_job_titles(page: Page):
    page.locator('span.oxd-topbar-body-nav-tab-item:has-text("Job")').click()
    page.locator('a.oxd-topbar-body-nav-tab-link:has-text("Job Titles")').click()

@when(parsers.parse(u'If "{job_title}" with "{job_description}" exist then delete it'))
def delete_job_title_if_exists(page: Page, job_title, job_description):
    sleep(1)
    element = page.get_by_role("row", name=f" {job_title} {job_description}  ").get_by_role("button").first
    if element.is_visible():
        element.click()
        page.locator('button[type="button"]:has-text("Yes, Delete")').click()


@when(u'Click Add button')
def click_add_button(page: Page):
    page.locator('button[type="button"]:has-text("Add")').click()

@when(parsers.parse(u'Set Job Title to "{job_title}"'))
def set_job_title(page: Page, job_title):
    page.locator(job_title_input_xp).fill(job_title)

@when(parsers.parse(u'Set Job Description to "{job_description}"'))
def set_job_description(page: Page, job_description):
    page.get_by_placeholder('Type description here').fill(job_description)

@when(u'Click Save button')
def click_save_button(page: Page):
    page.locator('button[type="submit"]:has-text("Save")').click()

@then(parsers.parse(u'Check if "{job_title}" appeares on page'))
def check_if_job_title_appears(page: Page, job_title):
    sleep(4)
    assert page.locator(f'//div[@data-v-6c07a142 and text()="{job_title}"]').is_visible()
