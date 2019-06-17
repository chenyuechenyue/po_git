from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SettingPage(BaseAction):
    display_button = By.XPATH,'//*[@text = "显示"]'
    def click_display(self):
        self.click(self.display_button)