from lib.Pages import tables
from selenium.webdriver.common.by import By
from lib.Enums.filters_enum import FiltersEnum
from lib.Helpers.helpers import wait_element_to_be_clickable, mylogger


filters_open_button = (By.XPATH, "//button[normalize-space()='Filters']")
onsite_filter_button = (By.XPATH, "//div[@role='group']/*/*[1]")
online_filter_button = (By.XPATH, "//div[@role='group']/*/*[2]")
apply_filter_button = (By.XPATH, f"//button[normalize-space()='{FiltersEnum.ApplyFilters.value}']")
hide_filter_button = (By.XPATH, "//button[normalize-space()='Hide']")
headers_filter_button = (By.XPATH, "//div[@class='p-multiselect-trigger']")
headers_filter_options = (By.XPATH, "//ul[@class='p-multiselect-items p-multiselect-list p-component']/*")
table_headers = (By.XPATH, "//thead[@class='p-datatable-thead']/tr/*")


def comparing_filtered_headers_list_with_displayed_headers(driver):
    wait_element_to_be_clickable(driver, *headers_filter_button)
    clicking_on_the_headers_filter_button(driver)
    wait_element_to_be_clickable(driver, *headers_filter_options)
    filter_items = driver.find_elements(*headers_filter_options)
    wait_element_to_be_clickable(driver, *table_headers)
    headers_elements = driver.find_elements(*table_headers)

    filtered_headers = []
    table_displayed_headers = []
    for filter_item in filter_items:
        filter_item_attribute = filter_item.get_attribute('class')
        if 'highlight' in filter_item_attribute:
            filtered_headers.append(filter_item.text)
    for header_item in headers_elements:
        table_displayed_headers.append(header_item.text)
    if filtered_headers == list(filter(None, table_displayed_headers)):
        mylogger("Headers are displayed as selected in filter")
        return True
    else:
        mylogger("Filtered headers and displayed table headers do not match")
        return False


def clicking_on_the_filter_button(driver):
    wait_element_to_be_clickable(driver, *filters_open_button)
    driver.find_element(*filters_open_button).click()


def clicking_on_the_headers_filter_button(driver):
    wait_element_to_be_clickable(driver, *headers_filter_button)
    driver.find_element(*headers_filter_button).click()


def checkign_DoA_Type_condition(driver):
    wait_element_to_be_clickable(driver, *onsite_filter_button)
    wait_element_to_be_clickable(driver, *online_filter_button)
    online_filter_text = driver.find_element(*online_filter_button).get_attribute("aria-pressed")
    onsite_filter_text = driver.find_element(*onsite_filter_button).get_attribute("aria-pressed")
    if online_filter_text == 'true' and onsite_filter_text == 'true':
        mylogger("Onsite and Online Doa filter types are selected")
    elif onsite_filter_text == 'true' and online_filter_text == 'false':
        mylogger("Onsite Doa filter type is selected")
    elif online_filter_text == 'true' and onsite_filter_text == 'false':
        mylogger("Online Doa filter type is selected")
    else:
        mylogger("Incorrect filter")


def selecting_online_filter(driver):
    wait_element_to_be_clickable(driver, *onsite_filter_button)
    wait_element_to_be_clickable(driver, *online_filter_button)
    online_filter_text = driver.find_element(*online_filter_button).get_attribute("aria-pressed")
    onsite_filter_text = driver.find_element(*onsite_filter_button).get_attribute("aria-pressed")
    if online_filter_text == 'true' and onsite_filter_text == 'true':
        mylogger("Selecting Online filter")
        driver.find_element(*onsite_filter_button).click()
    elif onsite_filter_text == 'true' and online_filter_text == 'false':
        mylogger("Selecting Online filter")
        driver.find_element(*online_filter_button).click()
        driver.find_element(onsite_filter_button).click()
    else:
        mylogger("aaa")


def selecting_onsite_filter(driver):
    wait_element_to_be_clickable(driver, *onsite_filter_button)
    mylogger("Clicking on the Onsite filter button")
    driver.find_element(*onsite_filter_button).click()


def clicking_apply_filter(driver):
    wait_element_to_be_clickable(driver, *apply_filter_button)
    mylogger("Clicking on the Apply filter button")
    driver.find_element(*apply_filter_button).click()


def clicking_hide_filter(driver):
    wait_element_to_be_clickable(driver, *hide_filter_button)
    mylogger("Clicking on the Hide filter button")
    driver.find_element(*hide_filter_button).click()


def filtering_the_DOA_table_by_online(driver):
    clicking_on_the_filter_button(driver)
    checkign_DoA_Type_condition(driver)
    selecting_online_filter(driver)
    checkign_DoA_Type_condition(driver)
    clicking_apply_filter(driver)
    clicking_hide_filter(driver)
    assert True == tables.checking_online_data_availability(
        driver,
        text_online=FiltersEnum.Online.value
    )
