from enum import Enum


class LeftSidebarEnum(Enum):
    Dashboard = 'bpm_tasks_id', 'Dashboard'
    DoAs = 'opportunities_id', 'DoAs'
    Assignments = 'assignments_id', 'Assignments'
    Candidates = 'candidates_id', 'Candidates'
    Management = 'manage_id', 'Management'
    Approved_payments = 'approved_payments_id', 'Approved payments'
    Explore = 'explore_id', 'Explore'

    def __init__(self, xpath_name, text):
        self.xpath_name = xpath_name
        self.text = text
        
