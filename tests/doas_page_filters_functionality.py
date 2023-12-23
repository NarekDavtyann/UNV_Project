from lib.Pages import login_page
from lib.Test_Data.test_data import superUser_username, superUser_password
from lib.Enums.left_sidebar_enum import LeftSidebarEnum
from lib.Enums.tables_enum import DoAsTableDisplayOptions
from lib.Enums.filters_enum import FiltersEnum
from lib.Helpers.helpers import setup_browser
from lib.Test_Data.test_data import page_title_main
from lib.Pages import tables, left_sidebar_items, filters


def checking_filters_functionality():
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

    # Navigating to DoAs page
    left_sidebar_items.click_left_sidebar_items_by_text(
        driver=driver_instance,
        text=LeftSidebarEnum.DoAs.sidebar_element_text
    )

    # Checking which table view is selected
    tables.table_data_display_condition(driver=driver_instance, index=DoAsTableDisplayOptions.Grid.display_option)

    # Selecting List table view
    tables.click_list_view_item(driver=driver_instance, index=DoAsTableDisplayOptions.List.display_option)

    # Checking which table view is selected
    tables.table_data_display_condition(driver=driver_instance, index=DoAsTableDisplayOptions.List.display_option)

    # Checking table headers
    assert True == filters.comparing_filtered_headers_list_with_displayed_headers(driver=driver_instance)

    # Filtering the table
    filters.clicking_on_the_filter_button(driver=driver_instance)
    filters.checkign_DoA_Type_condition(driver=driver_instance)
    filters.selecting_online_filter(driver=driver_instance)
    filters.checkign_DoA_Type_condition(driver=driver_instance)
    filters.clicking_apply_filter(driver=driver_instance)
    filters.clicking_hide_filter(driver=driver_instance)
    assert True == tables.checking_online_data_availability(
        driver=driver_instance,
        text_online=FiltersEnum.Online.value
    )

    driver_instance.quit()


if __name__ == "__main__":
    checking_filters_functionality()


