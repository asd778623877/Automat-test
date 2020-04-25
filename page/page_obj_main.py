from page.search_page import search_obj
from page.setting_search import Setting_search

class page_obj_main:
    def __init__(self,driver):
        self.driver=driver

    def re_search_page(self):
        return search_obj(self.driver)

    def re_setting_search(self):
        return Setting_search(self.driver)