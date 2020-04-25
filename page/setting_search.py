from Base.base import Base
import page

class Setting_search(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def search_cl(self):
        self.click_element(page.search_s)

    def search_put(self,text):
        self.input_element(page.search_p,text)

    def search_ret(self):
        self.click_element(page.search_r)
