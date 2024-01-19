from lib.Pages import login_page, left_sidebar_items, management_page
from lib.Test_Data.test_data import superUser_username, superUser_password
from lib.Enums.left_sidebar_enum import LeftSidebarEnum
from lib.Helpers.helpers import setup_browser
from lib.Test_Data.test_data import page_title_main


def check_management_sections_availability():
    # driver setup
    url = 'https://aks-stg-green.unv.org/'
    driver_instance = setup_browser(browser_type='chrome', url=url)

    # login to UNV
    login_page.login(
        driver=driver_instance,
        user_name=superUser_username,
        password=superUser_password,
        title_main=page_title_main
    )

    # Navigating to Management page
    left_sidebar_items.click_left_sidebar_items_by_text(
        driver=driver_instance,
        text=LeftSidebarEnum.Management.value
    )
    assert True == left_sidebar_items.return_sidebar_element_condition(
        driver=driver_instance,
        name=LeftSidebarEnum.Management.value
    )

    # Checking sections availability
    assert True == management_page.checking_sections_availabilty(driver=driver_instance)

    management_page.click_on_each_element(driver=driver_instance)
    driver_instance.quit()


if __name__ == '__main__':
    check_management_sections_availability()

