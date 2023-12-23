import time

from selenium.webdriver.common.by import By
from lib.Helpers.helpers import wait_element_to_be_clickable, mylogger
import logging

table_rows = (By.XPATH, "//tbody/tr")
pagination_dropdown = (By.XPATH, "//div[@class='p-dropdown p-component p-inputwrapper-filled']")
rows_data_quantity = (By.XPATH, "//span[@class='p-paginator-current']")


def _return_selected_pagination_value(value):
    return By.XPATH, f"//label[normalize-space()='{value}']"


def _return_pagination_dropdown_option_by_name(name):
    return By.XPATH, f"//li[@aria-label='{name}']"


def _return_pagination_numeration_item_by_page_number(page_number):
    return By.XPATH,  f"//button[normalize-space()='{page_number}']"


def select_page_number_by_name(driver, page_name):
    wait_element_to_be_clickable(driver, *_return_pagination_numeration_item_by_page_number(page_name))
    mylogger(f"Navigating to the {page_name} page")
    driver.find_element(*_return_pagination_numeration_item_by_page_number(page_name)).click()


def return_which_pagination_page_is_selected(driver, page_number):
    time.sleep(2)
    wait_element_to_be_clickable(driver, *_return_pagination_numeration_item_by_page_number(page_number))
    mylogger(f"The {page_number} is selected as page option")
    dropdown_option = driver.find_element(*_return_pagination_numeration_item_by_page_number(page_number)).get_attribute("class")
    if "highlight" in dropdown_option:
        return True
    else:
        return False


def pagination_dropdown_value_condition(driver, value):
    wait_element_to_be_clickable(driver, *_return_selected_pagination_value(value))
    text = driver.find_element(*_return_selected_pagination_value(value)).text
    if value in text:
        mylogger(f" The {value} is selected as pagination dropdown value")
        return True
    else:
        return False


def pagination_dropdown_click(driver):
    wait_element_to_be_clickable(driver, *pagination_dropdown)
    mylogger(f"Click on the pagination dropdown")
    driver.find_element(*pagination_dropdown).click()


def pagination_dropdown_option_selection_by_name(driver, name):
    wait_element_to_be_clickable(driver,  *_return_pagination_dropdown_option_by_name(name))
    mylogger(f"Selecting {name} pagination dropdown option")
    driver.find_element(*_return_pagination_dropdown_option_by_name(name)).click()


def return_dropdown_option_condition(driver, name):
    wait_element_to_be_clickable(driver, *_return_pagination_dropdown_option_by_name(name))
    mylogger("Checking dropdown option condition")
    dropdown_option = driver.find_element(*_return_pagination_dropdown_option_by_name(name)).get_attribute("class")
    if "highlight" in dropdown_option:
        return True
    else:
        return False


def checking_rows_and_selected_value_to_be_equal(driver, filter_count):
    filter_count = int(filter_count)
    wait_element_to_be_clickable(driver, *table_rows)
    all_count = _return_all_rows_data_quantity_text(driver)
    if all_count >= filter_count:
        if not filter_count == len(driver.find_elements(*table_rows)):
            raise ValueError(f"Incorrect {all_count} rows quantity {filter_count}")
    else:
        if not all_count == len(driver.find_elements(*table_rows)):
            raise ValueError(f"Incorrect {all_count} rows quantity {filter_count}")


def _return_all_rows_data_quantity_text(driver):
    wait_element_to_be_clickable(driver, *rows_data_quantity)
    text = driver.find_element(*rows_data_quantity).text
    quantity_main = text.split()
    return int(quantity_main[5])
