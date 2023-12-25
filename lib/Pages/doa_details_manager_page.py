from selenium.webdriver.common.by import By
from lib.Helpers.helpers import wait_element_to_be_clickable

created_doa_title = (By.XPATH, "//span[@class='doa-detail__header--title']")


def doa_title_text(driver):
    wait_element_to_be_clickable(driver, *created_doa_title)
    doa_title = driver.find_element(*created_doa_title).text
    return doa_title


