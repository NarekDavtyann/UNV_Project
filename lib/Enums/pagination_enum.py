from enum import Enum


class PaginationDropdownElementsEnum(Enum):
    pagination_dropdown_item_10 = '10'
    pagination_dropdown_item_25 = '25'
    pagination_dropdown_item_50 = '50'
    pagination_dropdown_item_100 = '100'
    pagination_dropdown_item_200 = '200'

    def __init__(self, item_str):
        self.item_str = item_str


class PaginationPageNumbersEnum(Enum):
    PAGE_1 = 1
    PAGE_2 = 2
    PAGE_3 = 3
    PAGE_4 = 4
    PAGE_5 = 5

    def __init__(self, page_number):
        self.page_number = page_number

