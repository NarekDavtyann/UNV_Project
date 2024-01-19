from lib.Pages import login_page
from lib.Test_Data.test_data import superUser_username, superUser_password
from lib.Enums.pagination_enum import PaginationDropdownElementsEnum, PaginationPageNumbersEnum
from lib.Enums.tables_enum import DashboardTaskTablesEnum
from lib.Helpers.helpers import setup_browser
from lib.Test_Data.test_data import page_title_main
from lib.Pages import pagination, tables, filters


def checking_pagination_and_table_rows():
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

    # Checking if active tab is selected by default
    assert True == tables.task_tables_condition(
        driver=driver_instance,
        text=DashboardTaskTablesEnum.Active.task_table
    )

    # Checking table headers
    assert True == filters.comparing_filtered_headers_list_with_displayed_headers(driver=driver_instance)

    # Checking selected page number
    assert True == pagination.return_which_pagination_page_is_selected(
        driver=driver_instance,
        page_number=PaginationPageNumbersEnum.PAGE_1.page_number
    )

    # Navigating to the second page
    pagination.select_page_number_by_name(
        driver=driver_instance,
        page_name=PaginationPageNumbersEnum.PAGE_2.page_number
    )

    # Checking selected page number  --->> bug the 1st page remains highlighted even if it is not selected
    assert True == pagination.return_which_pagination_page_is_selected(
        driver=driver_instance,
        page_number=PaginationPageNumbersEnum.PAGE_2.page_number
    )

    # checking pagination selected value
    assert True == pagination.pagination_dropdown_value_condition(
        driver=driver_instance,
        value=PaginationDropdownElementsEnum.pagination_dropdown_item_10.item_str
    )

    # Checking if the rows amount is similar to selected value
    pagination.checking_rows_and_selected_value_to_be_equal(
        driver=driver_instance,
        filter_count=PaginationDropdownElementsEnum.pagination_dropdown_item_10.item_str
    )

    # Selecting new value and checking if selected
    pagination.pagination_dropdown_click(driver=driver_instance)

    pagination.pagination_dropdown_option_selection_by_name(
        driver=driver_instance,
        name=PaginationDropdownElementsEnum.pagination_dropdown_item_25.item_str
    )
    assert True == pagination.pagination_dropdown_value_condition(
        driver=driver_instance,
        value=PaginationDropdownElementsEnum.pagination_dropdown_item_25.item_str
    )

    # Checking if the rows amount is similar to selected value
    pagination.checking_rows_and_selected_value_to_be_equal(
        driver=driver_instance,
        filter_count=PaginationDropdownElementsEnum.pagination_dropdown_item_25.item_str
    )

    # Selecting new value and checking if selected
    pagination.pagination_dropdown_click(driver=driver_instance)

    pagination.pagination_dropdown_option_selection_by_name(
        driver=driver_instance,
        name=PaginationDropdownElementsEnum.pagination_dropdown_item_50.item_str
    )

    assert True == pagination.pagination_dropdown_value_condition(
        driver=driver_instance,
        value=PaginationDropdownElementsEnum.pagination_dropdown_item_50.item_str
    )
    # rows amount is similar to selected value  --->> bug 48 instead of 50
    pagination.checking_rows_and_selected_value_to_be_equal(
        driver=driver_instance,
        filter_count=PaginationDropdownElementsEnum.pagination_dropdown_item_50.item_str
    )

    driver_instance.quit()


if __name__ == "__main__":
    checking_pagination_and_table_rows()
