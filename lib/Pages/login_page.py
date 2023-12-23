from selenium.webdriver.common.by import By
from lib.Helpers.helpers import wait_element_to_be_clickable, mylogger
from lib.Test_Data.test_data import page_title_main

login_button = By.XPATH, "//button[@aria-label='Login or sign up']" #navigateing to main login page
username_field = (By.XPATH, "//input[@id='signInName']")
password_field = (By.XPATH, "//input[@id='password']")
_main_sign_in_button = (By.XPATH, "//button[@id='next']")
behalf_button = (By.XPATH, "//div[@class='behalf-icon behalf-login']")
behalf_email_field = (By.XPATH, "//input[@name='email']")
behalf_login_button = (By.XPATH, "//button[normalize-space()='Login']")


def click_on_login_or_sign_up_button(driver):
    wait_element_to_be_clickable(driver, *login_button)
    mylogger("Navigate to the sign in page")
    driver.find_element(*login_button).click()


def insert_username(driver, username):
    wait_element_to_be_clickable(driver, *username_field)
    mylogger(f"Inserting {username} to email field")
    driver.find_element(*username_field).send_keys(username)


def insert_password(driver, password):
    mylogger(f"Inserting {password} to password field")
    driver.find_element(*password_field).send_keys(password)


def click_sign_in_(driver):
    mylogger("Signing in to UNV")
    driver.find_element(*_main_sign_in_button).click()


def _return_page_title(driver, title_main):
    if driver.title == title_main:
        mylogger('The user successfully signed in')
        return driver.title == title_main
    else:
        return mylogger('Sign-in process failed')


def login(driver, user_name, password, title_main=page_title_main):
    click_on_login_or_sign_up_button(driver)
    insert_username(driver=driver, username=user_name)
    insert_password(driver=driver, password=password)
    click_sign_in_(driver)
    assert True == _return_page_title(driver=driver, title_main=title_main)


def change_user_by_behalf_login(driver, user_email):
    mylogger(f"Changing to {user_email} user ")
    wait_element_to_be_clickable(driver, *behalf_button)
    driver.find_element(*behalf_button).click()
    wait_element_to_be_clickable(driver, *behalf_email_field)
    driver.find_element(*behalf_email_field).send_keys(user_email)
    wait_element_to_be_clickable(driver, *behalf_login_button)
    driver.find_element(*behalf_login_button).click()

