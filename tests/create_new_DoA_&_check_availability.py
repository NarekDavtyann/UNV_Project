from lib.Enums.doa_assignment_pop_up_enum import OnlineAssignmentExpertisDropdownEnum
from lib.Enums.doa_creation_enum import (
    TaskTypeDropdownOptionsEnum,
    HourPerWeekDropdownOptionsEnum,
    AssignmentCountryDropdownOpionsEnum,
    SustainableDevelopmentGoalDropdownOpionsEnum
)

from lib.Pages import login_page
from lib.Pages.doa_details_manager_page import return_created_doa_data
from lib.Enums.languages_enum import LanguagesEnum, LanguagesProficiencyEnum
from lib.Enums.left_sidebar_enum import LeftSidebarEnum
from lib.Helpers.helpers import setup_browser
from lib.Test_Data.test_data import page_title_main, host_Entity_username, host_Entity_password
from lib.Pages import left_sidebar_items, create_new_doa, languages_pop_up


def checking_newly_created_DOA_availability():

    # driver setup
    url = 'https://aks-stg-green.unv.org/'
    driver_instance = setup_browser(browser_type='chrome', url=url)

    # login to UNV
    login_page.login(
        driver=driver_instance,
        user_name=host_Entity_username,
        password=host_Entity_password,
        title_main=page_title_main
    )

    assert True == left_sidebar_items.return_sidebar_element_condition(
        driver=driver_instance,
        name=LeftSidebarEnum.Dashboard.xpath_name
    )

    # Navigating to DoAs page
    left_sidebar_items.click_left_sidebar_items_by_text(driver=driver_instance, text=LeftSidebarEnum.DoAs.text)

    assert True == left_sidebar_items.return_sidebar_element_condition(
        driver=driver_instance,
        name=LeftSidebarEnum.DoAs.xpath_name
    )

    # Opening the "NEW DOA PAGE"
    create_new_doa.click_on_the_New_DoA_button(driver=driver_instance)

    # Navigating to Online Doa creation
    create_new_doa.click_on_the_online_DoA_button(driver=driver_instance)
    assert True == create_new_doa.return_doa_type_condition(
        driver=driver_instance,
        doa_type=create_new_doa.online_doa_button_locator
    )

    # Completing required fields
    create_new_doa.completing_mandatory_fields_for_online_doa(
        driver=driver_instance,
        task_type=TaskTypeDropdownOptionsEnum.Administration.value,
        hours_week=HourPerWeekDropdownOptionsEnum.Option_1_5.value,
        country=AssignmentCountryDropdownOpionsEnum.Afghanistan.value,
        sustainable_goal=SustainableDevelopmentGoalDropdownOpionsEnum.No_poverty.value
    )

    # Adding language option
    languages_pop_up.adding_language(
        driver=driver_instance,
        language=LanguagesEnum.Armenian_eastern.value,
        proficiency_name=LanguagesProficiencyEnum.Mother_tongue.value
    )

    # Completing assignment
    create_new_doa.completing_Doa_assignment(
        driver=driver_instance,
        option_name=OnlineAssignmentExpertisDropdownEnum.Administration.value
    )

    # Submitting to UNV
    create_new_doa.submit_doa_to_UNV(driver=driver_instance)

    # Checking doa_availability
    assert return_created_doa_data(driver=driver_instance) == return_created_doa_data(driver=driver_instance)


    driver_instance.quit()


if __name__ == '__main__':
    checking_newly_created_DOA_availability()

