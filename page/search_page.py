from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SearchPage(BaseAction):
    input_button =By.XPATH,'//*[@text="搜索…"]'
    back_button = By.CLASS_NAME,'android.widget.ImageButton'
    def input_value(self,value):
        self.input(self.input_button,value)
    def click_back(self):
        self.click(self.back_button)