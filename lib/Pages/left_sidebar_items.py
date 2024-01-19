
from selenium.webdriver.common.by import By

from lib.Enums.left_sidebar_enum import LeftSidebarEnum
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


def selecting_and_checking_sidebar_condition(driver):
    assert True == return_sidebar_element_condition(driver, name=LeftSidebarEnum.Dashboard.xpath_name)
    click_left_sidebar_items_by_text(driver, text=LeftSidebarEnum.DoAs.text)
    assert True == return_sidebar_element_condition(driver, name=LeftSidebarEnum.DoAs.xpath_name)
    click_left_sidebar_items_by_text(driver, text=LeftSidebarEnum.Assignments.text)
    assert True == return_sidebar_element_condition(driver, name=LeftSidebarEnum.Assignments.xpath_name)
    click_left_sidebar_items_by_text(driver, text=LeftSidebarEnum.Candidates.text)
    assert True == return_sidebar_element_condition(driver, name=LeftSidebarEnum.Candidates.xpath_name)
    click_left_sidebar_items_by_text(driver, text=LeftSidebarEnum.Management.text)
    assert True == return_sidebar_element_condition(driver, name=LeftSidebarEnum.Management.xpath_name)
    click_left_sidebar_items_by_text(driver, text=LeftSidebarEnum.Approved_payments.text)
    assert True == return_sidebar_element_condition(driver, name=LeftSidebarEnum.Approved_payments.xpath_name)
    click_left_sidebar_items_by_text(driver, text=LeftSidebarEnum.Explore.text)
    assert True == return_sidebar_element_condition(driver, name=LeftSidebarEnum.Explore.xpath_name)
    click_left_sidebar_items_by_text(driver, text=LeftSidebarEnum.Dashboard.text)
    assert True == return_sidebar_element_condition(driver, name=LeftSidebarEnum.Dashboard.xpath_name)
    
    