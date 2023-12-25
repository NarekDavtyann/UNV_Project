from selenium.webdriver.common.by import By

from lib.Helpers.helpers import wait_element_to_be_clickable, mylogger, random_file_name, random_numbers


# X-path
create_new_doa_button_locator = (By.XPATH, "//button[@data-testId='topbar-msal-newDoa']")
onsite_doa_button_locator = (By.XPATH, "//div[@class='input out-form']//div[@role='group']/*/*[1]")
online_doa_button_locator = (By.XPATH, "//div[@class='input out-form']//div[@role='group']/*/*[2]")

online_new_assignment_button_locator = (By.XPATH, "//span[normalize-space()='New']")

assignment_expertise_required_dropdown_button = (By.XPATH, "//div[@data-testid='primaryTask']//div[@class='p-dropdown p-component']")

doa_title_locator = (By.XPATH, "//input[@placeholder='Type a short title']")
task_description_locator = (By.XPATH, "//textarea[@name='taskDescription']")
duration_locator = (By.XPATH, "//input[@name='duration']")
assignment_context_locator = (By.XPATH, "//textarea[@name='context']")
number_of_assignments_locator = (By.XPATH, "//input[@name='volunteersNumber']")
required_skills_locator = (By.XPATH, "//textarea[@name='requiredSkillExperience']")

task_type_dropdown_locator = (By.XPATH, "//div[@data-testid='taskType']//div[@class='p-dropdown p-component']")
hours_per_week_dropdown_locator = (By.XPATH, "//div[@data-testid='hoursWeek']//div[@class='p-dropdown p-component']")
assignment_country_dropdown_locator = (By.XPATH, "//div[@data-testid='country']//div[@class='p-dropdown p-component']")
sustainable_development_goal_dropdown_locator = (By.XPATH, "//div[@data-testid='sdgType']//div[@class='p-dropdown p-component']")


task_administration = (By.XPATH, "//li[@aria-label='Administration']")
hours_per_week = (By.XPATH, "//li[@aria-label='+ 20']")
country_afghanistan = (By.XPATH, "//li[@aria-label='Afghanistan']")
stg_no_poverty = (By.XPATH, "//li[@aria-label='1. No poverty']")

assignment_continue = (By.XPATH, "//span[normalize-space()='Continue']")
doa_submit_button = (By.XPATH, "//button[normalize-space()='Submit to UNV']")

confirm_doa_creation_button = (By.XPATH, "//button[normalize-space()='Complete']")

def click_on_the_New_DoA_button(driver):
    wait_element_to_be_clickable(driver, *create_new_doa_button_locator)
    mylogger("Navigating to the NEW DoA creation page")
    driver.find_element(*create_new_doa_button_locator).click()


def click_on_the_online_DoA_button(driver):
    wait_element_to_be_clickable(driver, *online_doa_button_locator)
    mylogger("Navigating to the DoA creation page")
    driver.find_element(*online_doa_button_locator).click()


def return_doa_type_condition(driver, doa_type):
    wait_element_to_be_clickable(driver, *doa_type)
    element = driver.find_element(*doa_type)
    if element.get_attribute('aria-pressed') == 'true':
        mylogger(f"The corresponding DoA type is selected")
        return True
    else:
        return False


def set_and_return_doa_title_field(driver):
    wait_element_to_be_clickable(driver, *doa_title_locator)
    mylogger("Completing the 'Doa title' field")
    doa_title = random_file_name()
    driver.find_element(*doa_title_locator).send_keys(doa_title)
    return doa_title


def set_and_return_task_description_field(driver):
    wait_element_to_be_clickable(driver, *task_description_locator)
    mylogger("Completing 'Task description' field")
    task_description = random_file_name()
    driver.find_element(*task_description_locator).send_keys(task_description)
    return task_description


def set_and_return_duration_in_weeks_field(driver):
    wait_element_to_be_clickable(driver, *duration_locator)
    mylogger("Completing 'Duration' field")
    duration = random_numbers()
    driver.find_element(*duration_locator).send_keys(duration)
    return duration


def set_and_return_assignment_context_field(driver):
    wait_element_to_be_clickable(driver, *assignment_context_locator)
    mylogger("Completing 'Assignment context' field")
    assignment_context = random_file_name()
    driver.find_element(*assignment_context_locator).send_keys(assignment_context)
    return assignment_context


def set_and_return_number_of_assignments_field(driver):
    wait_element_to_be_clickable(driver, *assignment_context_locator)
    mylogger("Completing 'Number of assignments' field")
    assignment_numbers = random_numbers()
    driver.find_element(*number_of_assignments_locator).send_keys(assignment_numbers)
    return assignment_numbers


def set_and_return_required_skills_fields(driver):
    wait_element_to_be_clickable(driver, *required_skills_locator)
    mylogger("Completing 'Required skills' field")
    required_skills = random_file_name()
    driver.find_element(*required_skills_locator).send_keys(required_skills)
    return required_skills

    
def clicking_on_task_type_dropdown(driver):
    wait_element_to_be_clickable(driver, *task_type_dropdown_locator)
    driver.find_element(*task_type_dropdown_locator).click()


def clicking_on_hours_per_week_dropdown(driver):
    wait_element_to_be_clickable(driver, *hours_per_week_dropdown_locator)
    driver.find_element(*hours_per_week_dropdown_locator).click()


def clicking_on_assingment_country_dropdown(driver):
    wait_element_to_be_clickable(driver, *assignment_country_dropdown_locator)
    driver.find_element(*assignment_country_dropdown_locator).click()


def clicking_on_sustainable_development_goal_dropdown(driver):
    wait_element_to_be_clickable(driver, *sustainable_development_goal_dropdown_locator)
    driver.find_element(*sustainable_development_goal_dropdown_locator).click()


def _return_dropdown_option_by_name(option_name):
    return By.XPATH, f"//li[@aria-label='{option_name}']"
    
    
def click_on_dropdown_option_by_name(driver, option_name):
    wait_element_to_be_clickable(driver, *_return_dropdown_option_by_name(option_name))
    mylogger(f"Selecting {option_name} dropdown option")
    driver.find_element(*_return_dropdown_option_by_name(option_name)).click()
    

def click_on_online_new_assignment_button(driver):
    wait_element_to_be_clickable(driver, *online_new_assignment_button_locator)
    driver.find_element(*online_new_assignment_button_locator).click()


def click_on_the_expertise_is_required_drpodown(driver):
    wait_element_to_be_clickable(driver, *assignment_expertise_required_dropdown_button)
    driver.find_element(*assignment_expertise_required_dropdown_button).click()


def _return_expertise_dropdown_option(option_name):
    return (By.XPATH,
            f"//div[@class='p-dropdown-panel p-hidden p-input-overlay p-input-overlay-visible']"
            f"//li[@aria-label='{option_name}'][normalize-space()='{option_name}']"
            )


def click_on_expertise_is_required_dropdown_option(driver, option_name):
    wait_element_to_be_clickable(driver, *_return_expertise_dropdown_option(option_name))
    driver.find_element(*_return_expertise_dropdown_option(option_name)).click()


def click_on_assignment_continue(driver):
    wait_element_to_be_clickable(driver, *assignment_continue)
    mylogger("Assignment is completed")
    driver.find_element(*assignment_continue).click()


def click_on_complete_button_in_confirmation_pop_up(driver):
    wait_element_to_be_clickable(driver, *confirm_doa_creation_button)
    driver.find_element(*confirm_doa_creation_button).click()


def completing_mandatory_fields_for_online_doa(driver, task_type, hours_week, country, sustainable_goal):
    doa_title = set_and_return_doa_title_field(driver=driver)
    doa_task_desc = set_and_return_task_description_field(driver=driver)
    doa_duration = set_and_return_duration_in_weeks_field(driver=driver)
    set_and_return_assignment_context_field(driver=driver)
    doa_assignment_number = set_and_return_number_of_assignments_field(driver=driver)
    set_and_return_required_skills_fields(driver=driver)
    clicking_on_task_type_dropdown(driver=driver)
    click_on_dropdown_option_by_name(driver=driver, option_name=task_type)
    clicking_on_hours_per_week_dropdown(driver=driver)
    click_on_dropdown_option_by_name(driver=driver, option_name=hours_week)
    clicking_on_assingment_country_dropdown(driver=driver)
    click_on_dropdown_option_by_name(driver=driver, option_name=country)
    clicking_on_sustainable_development_goal_dropdown(driver=driver)
    click_on_dropdown_option_by_name(driver=driver, option_name=sustainable_goal)
    mylogger('All required fields are completed')

    return [doa_title, doa_task_desc, doa_duration, doa_assignment_number]


def completing_Doa_assignment(driver, option_name):
    click_on_online_new_assignment_button(driver)
    click_on_the_expertise_is_required_drpodown(driver)
    click_on_expertise_is_required_dropdown_option(driver, option_name)
    click_on_assignment_continue(driver)


def submit_doa_to_UNV(driver):
    wait_element_to_be_clickable(driver, *doa_submit_button)
    mylogger('Doa is created and submitted to UNV')
    driver.find_element(*doa_submit_button).click()
    click_on_complete_button_in_confirmation_pop_up(driver)


def return_iserted_data_value(driver):
    doa_title = set_and_return_doa_title_field(driver)
    doa_task_desc = set_and_return_task_description_field(driver)
    doa_duration = set_and_return_duration_in_weeks_field(driver)
    doa_number_of_assignments = set_and_return_number_of_assignments_field(driver)

    return [doa_title, doa_task_desc, doa_duration, doa_number_of_assignments]