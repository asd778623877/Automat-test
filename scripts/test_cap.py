import pytest
from Base import init_driver
from page.page_obj_main import page_obj_main
class Test_cap:

    def setup_class(self):
        self.driver=init_driver()
        self.obj_o=page_obj_main(self.driver)


    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("name,pwd",[("fly","123"),("tnar","334")])
    def test_login(self,name,pwd):
        self.obj_o.re_search_page().name_input(name)
        self.obj_o.re_search_page().pwd_input(pwd)
        self.obj_o.re_search_page().click_login()
        assert True