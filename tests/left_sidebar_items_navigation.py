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
    assert True == left_sidebar_items.return_sidebar_element_condition(
        driver=driver_instance,
        name=LeftSidebarEnum.Dashboard.sidebar_element_xpath_name
    )

    left_sidebar_items.click_left_sidebar_items_by_text(
        driver=driver_instance,
        text=LeftSidebarEnum.DoAs.sidebar_element_text
    )
    assert True == left_sidebar_items.return_sidebar_element_condition(
        driver=driver_instance,
        name=LeftSidebarEnum.DoAs.sidebar_element_xpath_name
    )

    left_sidebar_items.click_left_sidebar_items_by_text(
        driver=driver_instance,
        text=LeftSidebarEnum.Assignments.sidebar_element_text
    )

    assert True == left_sidebar_items.return_sidebar_element_condition(
        driver=driver_instance,
        name=LeftSidebarEnum.Assignments.sidebar_element_xpath_name
    )

    left_sidebar_items.click_left_sidebar_items_by_text(
        driver=driver_instance,
        text=LeftSidebarEnum.Candidates.sidebar_element_text

    )

    assert True == left_sidebar_items.return_sidebar_element_condition(
        driver=driver_instance,
        name=LeftSidebarEnum.Candidates.sidebar_element_xpath_name
    )

    left_sidebar_items.click_left_sidebar_items_by_text(
        driver=driver_instance,
        text=LeftSidebarEnum.Management.sidebar_element_text
    )

    assert True == left_sidebar_items.return_sidebar_element_condition(
        driver=driver_instance,
        name=LeftSidebarEnum.Management.sidebar_element_xpath_name
    )

    left_sidebar_items.click_left_sidebar_items_by_text(
        driver=driver_instance,
        text=LeftSidebarEnum.Approved_payments.sidebar_element_text
    )

    assert True == left_sidebar_items.return_sidebar_element_condition(
        driver=driver_instance,
        name=LeftSidebarEnum.Approved_payments.sidebar_element_xpath_name
    )

    left_sidebar_items.click_left_sidebar_items_by_text(
        driver=driver_instance,
        text=LeftSidebarEnum.Explore.sidebar_element_text
    )

    assert True == left_sidebar_items.return_sidebar_element_condition(
        driver=driver_instance,
        name=LeftSidebarEnum.Explore.sidebar_element_xpath_name
    )

    left_sidebar_items.click_left_sidebar_items_by_text(
        driver=driver_instance,
        text=LeftSidebarEnum.Dashboard.sidebar_element_text
    )

    assert True == left_sidebar_items.return_sidebar_element_condition(
        driver=driver_instance,
        name=LeftSidebarEnum.Dashboard.sidebar_element_xpath_name
    )
    driver_instance.quit()


if __name__ == "__main__":
    check_sidebar_navigation()
