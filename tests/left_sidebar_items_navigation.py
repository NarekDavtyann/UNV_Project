from lib.Enums.left_sidebar_enum import LeftSidebarEnum
from lib.Pages import left_sidebar_items
from lib.Pages import login_page
from lib.Helpers import helpers
from lib.Test_Data.test_data import superUser_username, superUser_password


def check_sidebar_navigation():
    # driver setup
    url = 'https://aks-stg-green.unv.org/'
    driver_instance = helpers.setup_browser(browser_type='chrome', url=url)

    # login to unv
    login_page.login(driver=driver_instance, user_name=superUser_username, password=superUser_password)

    # sidebar elements click
    left_sidebar_items.selecting_and_checking_sidebar_condition(driver=driver_instance)
    driver_instance.quit()


if __name__ == "__main__":
    check_sidebar_navigation()
