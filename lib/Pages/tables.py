import time
from selenium.webdriver.common.by import By
from lib.Helpers.helpers import wait_element_to_be_clickable, mylogger


tab_tasks_buttons = (By.XPATH, "//ul[@class='tab-navigation']/*")
data_type = (By.XPATH, "//tbody/tr/*[2]/span")


def task_tables_condition(driver, text):
    wait_element_to_be_clickable(driver, *tab_tasks_buttons)
    table_value = driver.find_elements(*tab_tasks_buttons)
    for element in table_value:
        if element.text == text:
            mylogger(f"The {text} task table is selected")
            return True
        else:
            return False


def _return_data_display_option_by_index(index):
    return By.XPATH, f"//div[@class='data-display__selector']/*[{index}]"


def table_data_display_condition(driver, index):
    time.sleep(2)
    wait_element_to_be_clickable(driver, *_return_data_display_option_by_index(index))
    text = driver.find_element(*_return_data_display_option_by_index(index)).get_attribute("class")
    if "active" in text and index == 1:
        mylogger(f"The Grid view is selected")
    elif "active" in text and index == 2:
        mylogger(f"The List view is selected")
    else:
        raise Exception


def click_list_view_item(driver, index):
    driver.find_element(*_return_data_display_option_by_index(index)).click()


def checking_onsite_data_availability(driver, text_onsite):
    wait_element_to_be_clickable(driver, *data_type)
    doa_type = driver.find_elements(*data_type)
    for element in doa_type:
        if element.text != text_onsite:
            mylogger("Filter is incorrect")
            return False
    mylogger("Onsite Doas are only shown")
    return True


def checking_online_data_availability(driver, text_online):
    wait_element_to_be_clickable(driver, *data_type)
    doa_type = driver.find_elements(*data_type)
    for element in doa_type:
        if element.text != text_online:
            mylogger("Filter is incorrect")
            return False
    mylogger("Onsite Doas are only shown")
    return True

