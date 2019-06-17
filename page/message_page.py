from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MessagePage(BaseAction):
    new_add = By.ID,'com.android.mms:id/action_compose_new'
    def click_new_add(self):
        self.click(self.new_add)
