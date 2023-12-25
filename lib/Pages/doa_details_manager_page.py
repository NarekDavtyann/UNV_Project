from selenium.webdriver.common.by import By
from lib.Helpers.helpers import wait_element_to_be_clickable

created_doa_title = (By.XPATH, "//span[@class='doa-detail__header--title']")
created_doa_task_description = (By.XPATH, "//div[@class='section']/div[4]/p[1]")
created_doa_duration = (
    By.XPATH,
    "//div[@class='two-column'][1]/div[@class='section__column'][2]/div[@class='section_item'][3]"
)

created_doa_number_of_assignments = (
    By.XPATH,
    "//div[@class='two-column'][1]/div[@class='section__column'][2]/div[@class='section_item'][4]"
)

def _return_doa_title_text(driver):
    wait_element_to_be_clickable(driver, *created_doa_title)
    doa_title = driver.find_element(*created_doa_title).text
    return doa_title


def _return_doa_task_description(driver):
    wait_element_to_be_clickable(driver, *created_doa_title)
    doa_task_description = driver.find_element(*created_doa_title).text
    return doa_task_description


def _return_doa_duration_in_weeks(driver):
    wait_element_to_be_clickable(driver, *created_doa_duration)
    doa_duration_text = driver.find_element(*created_doa_duration).text
    doa_duration = doa_duration_text.split()
    return doa_duration[1]


def _return_doa_assignments_number(driver):
    wait_element_to_be_clickable(driver, *created_doa_number_of_assignments)
    assignment_number = driver.find_element(*created_doa_number_of_assignments).text
    return assignment_number


def return_created_doa_data(driver):
    doa_title = _return_doa_title_text(driver)
    created_doa_task_desc = _return_doa_task_description(driver)
    doa_duration = _return_doa_duration_in_weeks(driver)
    doa_assignment_number = _return_doa_assignments_number(driver)

    return [doa_title, created_doa_task_desc, doa_duration, doa_assignment_number]

