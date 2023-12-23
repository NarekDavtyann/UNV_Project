from enum import Enum


class RequiredDropdownsEnum(Enum):
    Task_type = 'taskType'
    Hours_per_week = 'hoursWeek'
    Assignment_country = 'country'
    Sustainable_Development_Goal = 'sdgType'


class HourPerWeekDropdownOptionsEnum(Enum):
    Option_20 = '+ 20'
    Option_1_5 = '1 - 5'
    Option_11_20 = '11 - 20'
    Option_6_10 = '6 - 10'


class TaskTypeDropdownOptionsEnum(Enum):
    Administration = 'Administration'


class AssignmentCountryDropdownOpionsEnum(Enum):
    Afghanistan = 'Afghanistan'


class SustainableDevelopmentGoalDropdownOpionsEnum(Enum):
    No_poverty = '1. No poverty'



