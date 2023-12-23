
from selenium.webdriver.common.by import By
from lib.Helpers.helpers import wait_element_to_be_clickable, mylogger

sidebar_elements_xpath = (By.XPATH, "//div[@class='user-nav']/a")


def _return_item_by_name(name):
    return By.XPATH, f"//a[@data-testid='{name}']"


def return_sidebar_element_condition(driver, name):
    mylogger(f'Checking section condition')
    wait_element_to_be_clickable(driver, *_return_item_by_name(name))
    if "active" in driver.find_element(*_return_item_by_name(name)).get_attribute("class"):
        return True
    else:
        return False





def click_left_sidebar_items_by_text(driver, text):
    wait_element_to_be_clickable(driver, *sidebar_elements_xpath)
    elements = driver.find_elements(*sidebar_elements_xpath)
    for element in elements:
        if element.text == text:
            mylogger(f'Navigating to {text} page')
            element.click()
            break
