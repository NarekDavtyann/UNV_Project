from enum import Enum


class ManagementSectionsEnum(Enum):
    HostEntities = 'Host entities'
    Donors = 'Donors'
    DoaTemplates = 'DoaTemplates'
    Tags = 'Tags'
    Documents = 'Documents'
    SystemEmails = 'System emails'
    MasterTables = 'MasterTables'
    MassEmailTemplates = 'Mass email templates'
    LoginAs = 'Login as'
    HangFireDashboard = 'HangFire dashboard'

    def __init__(self, sections):
        self.sections = sections

