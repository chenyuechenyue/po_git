from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddAddressPage(BaseAction):
    name =By.XPATH,'//*[@text="姓名"]'
    phone =By.XPATH,'//*[@text="电话"]'
    def input_name(self,value):
        self.input(self.name,value)
    def input_phone(self,value):
        self.input(self.phone,value)
