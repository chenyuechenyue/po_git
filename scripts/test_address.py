from base.base_driver import init_driver
from page.page import Page


class TestAddress:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
    def teardown(self):
        pass
    def test_address(self):
        self.page.address().click_address_add_list()
        self.page.add_address().input_name('张明伟')
        self.page.add_address().input_phone('18730555358')