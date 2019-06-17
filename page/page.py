from page.add_address_page import AddAddressPage
from page.address_page import AddressPage
from page.display_page import DisplayPage
from page.message_page import MessagePage
from page.new_message_page import NewMessagePage
from page.search_page import SearchPage
from page.setting_page import SettingPage


class Page:
    def __init__(self,driver):
        self.driver = driver
    def setting(self):
        return SettingPage(self.driver)
    def display(self):
        return DisplayPage(self.driver)
    def search(self):
        return SearchPage(self.driver)
    def message(self):
        return MessagePage(self.driver)
    def new_message(self):
        return NewMessagePage(self.driver)
    def address(self):
        return AddressPage(self.driver)
    def add_address(self):
        return AddAddressPage(self.driver)