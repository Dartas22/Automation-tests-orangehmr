from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from pytest_bdd import scenario, given, when, then, parsers
from time import sleep
import sys
sys.path.append('D:\\VC\\testing_proj\\tests\\features')

PATH = "C:\\Program Files (x86)\\chrome-win64\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = ChromeService(executable_path=PATH)
driver = webdriver.Chrome(service=service, options=options)

loginB = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
passB = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
loginButton = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

assignClaimB = '//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/div[1]/button'
employeeName = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div/div/input'
eventSelect = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/div[1]'
currencySelect = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[1]'
remarksInp = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/textarea'

createButton = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/button[2]'
assign_claim = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/h6'


@scenario('..\\..\\add_claim.feature', 'Add claim')
def test_add_claim():
    pass

@given(u'Opem Orange HRM on Claim page')
def open_home_page():
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/claim/viewAssignClaim')
    sleep(2)

@when(parsers.parse(u'Login to Orange HRM with "{user}" and "{password}"'))
def login(user, password):
    driver.find_element(By.XPATH, loginB).send_keys(user)
    driver.find_element(By.XPATH, passB).send_keys(password)
    driver.find_element(By.XPATH, loginButton).click()
    sleep(2)

@when(u'Click Assign Claim button')
def click_asign():
    driver.find_element(By.XPATH, assignClaimB).click()
    sleep(2)

@when(parsers.parse(u'Input empleyee name "{employee}"'))
def input_emp(employee):
    driver.find_element(By.XPATH, employeeName).send_keys(employee)
    sleep(2)
    driver.find_element(By.XPATH, employeeName).send_keys(Keys.DOWN)
    driver.find_element(By.XPATH, employeeName).send_keys(Keys.RETURN)

@when(parsers.parse(u'Select Event "{event}"'))
def inp_event(event):
    driver.find_element(By.XPATH, eventSelect).send_keys(event, Keys.RETURN)

@when(parsers.parse(u'Select Currency "{currency}"'))
def step_imp(currency):
    driver.find_element(By.XPATH, eventSelect).send_keys(Keys.TAB, currency, Keys.RETURN)

@when(parsers.parse(u'Add remark "{desc}"'))
def step_imp(desc):
    driver.find_element(By.XPATH, remarksInp).send_keys(desc)

@when(u'Click Create button')
def step_imp():
    driver.find_element(By.XPATH, createButton).click()
    sleep(5)

@then(u'Check if Assign Claim displays')
def step_imp():
    ac_display = driver.find_element(By.XPATH, assign_claim).is_displayed()
    assert ac_display
