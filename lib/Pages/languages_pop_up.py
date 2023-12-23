from selenium.webdriver.common.by import By
from lib.Helpers.helpers import wait_element_to_be_clickable, mylogger

add_language_button = (By.XPATH, "//span[normalize-space()='Add language']")
language_dropdown = (By.XPATH, "//label[normalize-space()='Select one language']")
language_proficiency_dropdown = (By.XPATH, "//label[normalize-space()='Select the level of knowledge']")
language_submit_button = (By.XPATH, "//button[@type='submit']//span[@class='p-button-text p-c'][normalize-space()='Add language']")
language_list = (By.XPATH, "")


def click_on_add_language_button(driver):
    wait_element_to_be_clickable(driver, *add_language_button)
    driver.find_element(*add_language_button).click()


def click_on_language_dropdown(driver):
    wait_element_to_be_clickable(driver, *language_dropdown)
    driver.find_element(*language_dropdown).click()


def click_on_laguage_proficiency_dropdown(driver):
    wait_element_to_be_clickable(driver, *language_proficiency_dropdown)
    driver.find_element(*language_proficiency_dropdown).click()


def submit_language(driver):
    wait_element_to_be_clickable(driver, *language_submit_button)
    driver.find_element(*language_submit_button).click()


def _return_language_option(language):
    return By.XPATH, f"//li[@aria-label='{language}']"


def _return_language_proficiency_option(proficiency_name):
    return By.XPATH, f"//li[@aria-label='{proficiency_name}']"


def click_on_language_option(driver, language):

    driver.find_element(*_return_language_option(language)).click()


def click_on_language_proficency_option(driver, proficiency_name):
    wait_element_to_be_clickable(driver, *_return_language_proficiency_option(proficiency_name))
    driver.find_element(*_return_language_proficiency_option(proficiency_name)).click()


def adding_language(driver, language, proficiency_name):
    click_on_add_language_button(driver)
    click_on_language_dropdown(driver)
    click_on_language_option(driver, language)
    click_on_laguage_proficiency_dropdown(driver)
    click_on_language_proficency_option(driver, proficiency_name)
    submit_language(driver)
    mylogger(f"{language} language option  is added")
