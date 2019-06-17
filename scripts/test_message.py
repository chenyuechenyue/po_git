import pytest

from base.base_driver import init_driver
from page.page import Page


class TestMessage:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
    def teardown(self):
        pass
    # @pytest.mark.parametrize(('name','value'),[('123','aaa'),('456'),('bbg')])
    @pytest.mark.parametrize(("name", "content"), [("zhangsan", "hello"), ("lisi", "hello123")])
    def test_message(self,name,content):
        self.page.message().click_new_add()
        self.page.new_message().input_person(name)
        self.page.new_message().input_values(content)
        self.page.new_message().click_send()