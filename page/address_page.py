from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressPage(BaseAction):
    address_list = By.ID,'com.android.contacts:id/floating_action_button'
    def click_address_add_list(self):
        self.click(self.address_list)