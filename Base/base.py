from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Base:

    def __init__(self,driver):
        self.driver = driver

    def find_elementI(self,loc,timeout=10,poll=0.5):
        '''

        :param loc: 元素，元祖类型
        :param timeout: 超时时间为10s
        :param poll: 0.5s搜索一次
        :return: 返回找到的元素
        '''
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))

    def click_element(self,loc):
        '''

        :param loc: 元素，元祖类型
        :return: 无
        '''
        self.find_elementI(loc).click()

    def input_element(self,loc,text):
        '''

        :param loc: 元素，元祖类型
        :param text: 文本
        :return:
        '''
        self.find_elementI(loc).clear()
        self.find_elementI(loc).send_keys(text)

    def key_search(self):
        self.driver.keyevent(84)
