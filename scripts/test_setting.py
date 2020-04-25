from Base.init_driver import init_driver
from page.page_obj_main import page_obj_main
from Base.read_date import ret_yaml_date
import pytest

def ret_data():
    data=ret_yaml_date("search_date").get("search_date")
    set_data_list=[]
    for i in data.keys():
        set_data_list.append((i,data.get(i).get("test")))
    return set_data_list
class Test_set:

    def setup_class(self):
        self.driver=init_driver()
        self.search_obj=page_obj_main(self.driver)
        self.search_obj.re_setting_search().search_cl()

    def teardown_class(self):
        self.search_obj.re_setting_search().search_ret()
        self.driver.quit()

    @pytest.mark.parametrize("name,text",ret_data())
    def test_set_se(self,name,text):
        print("测试用例：%s" % name)
        self.search_obj.re_setting_search().search_put(text)
        self.driver.get_screenshot_as_file("./picture/%s.png"% name)