from base.base_driver import init_driver

from page.page import Page


class TestDisplay:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        pass

    def test_srarch(self):
        self.page.setting().click_display()
        self.page.display().click_search()
        self.page.search().input_value('hello')
        self.page.search().click_back()
