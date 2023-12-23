from enum import Enum


class DashboardTaskTablesEnum(Enum):
    Active = 'Active'
    Completed = 'Completed'

    def __init__(self, task_table):
        self.task_table = task_table


class DoAsTableDisplayOptions(Enum):
    Grid = 1
    List = 2

    def __init__(self, display_option):
        self.display_option = display_option


class CandidateTasktableenum(Enum):
    Active = 'Active'
    Archived = 'Archived'

    def __init__(self,task_table):
        self.task_table = task_table

