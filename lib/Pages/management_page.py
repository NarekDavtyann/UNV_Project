import logging
from selenium.webdriver.common.by import By
from lib.Helpers.helpers import wait_element_to_be_clickable, mylogger


management_sections = (By.XPATH, "//div[@class='manage-panel__section']/*/a")


def _return_section_element(section_name):
    return By.XPATH, f"//div[@class='uvp-card__content'][normalize-space()='{section_name}']"


def clicking_on_the_section_by_name(driver, section_name):
    wait_element_to_be_clickable(driver, *_return_section_element(section_name))
    driver.find_element(*_return_section_element(section_name)).click()


def checking_sections_availabilty(driver):
    wait_element_to_be_clickable(driver, *management_sections)
    sections_label = []
    section_elements = driver.find_elements(*management_sections)
    for item in section_elements:
        sections_label.append(item.text)
    if len(sections_label) < 10:
        mylogger('Section is missing')
        return False
    elif len(sections_label) > 10:
        mylogger('New section is added')
    else:
        mylogger('All sections are displayed')
        return True


def click_on_each_element(driver):
    sections_label = []
    section_elements = driver.find_elements(*management_sections)
    for item in section_elements:
        sections_label.append(item.text)
    current_url = driver.current_url
    for each_item in sections_label:
        if len(sections_label) == 10:
            mylogger(f"Navigating to the {each_item} pa")
            wait_element_to_be_clickable(driver, *_return_section_element(each_item))
            driver.find_element(*_return_section_element(each_item)).click()
            driver.get(current_url)



