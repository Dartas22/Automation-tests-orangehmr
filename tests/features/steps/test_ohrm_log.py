from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from pytest_bdd import scenario, given, when, then, parsers
from time import sleep
import sys
sys.path.append('D:\\VC\\testing_proj\\tests\\features')

# Ścieżka do pliku wykonywalnego chromedriver.exe

loginB = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
passB = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
loginButton = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
dashboard = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a'

PATH = "C:\\Program Files (x86)\\chrome-win64\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = ChromeService(executable_path=PATH)
driver = webdriver.Chrome(service=service, options=options)

@scenario('..\\ohrm_log.feature', 'Succesfully login to OrangeHRM')
def test_login():
    pass

@given(u'I open HRM Homepage')
def open_home_page():
    driver.get('https://opensource-demo.orangehrmlive.com/')
    sleep(2)


@when(parsers.parse(u'Enter username "{user}" and password "{pwd}"'))
def input_data(user, pwd):
    driver.find_element(By.XPATH, loginB).send_keys(user)
    driver.find_element(By.XPATH, passB).send_keys(pwd)


@when(u'Click on login button')
def click_login_button():
    driver.find_element(By.XPATH, loginButton).click()

@then(u'User must successfully login to the Dashboard page')
def sucesfull_login():
    sleep(2)
    try:
        db = driver.find_element(By.XPATH, dashboard).is_displayed()
    except:
        driver.close()
        assert False, "Test Failed"

    if db is True:
        driver.close()
        assert True, "Test Passed"
