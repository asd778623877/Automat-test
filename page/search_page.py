
import page
from Base.base import Base
from selenium.webdriver.common.keys import Keys

class search_obj(Base):

    def __init__(self,driver):
        Base.__init__(self,driver)

    def name_input(self,text):
        self.input_element(page.tnar_n,text)


    def pwd_input(self,date):
        self.input_element(page.tnar_p,date)

    def click_login(self):
        self.click_element(page.tnar_e)