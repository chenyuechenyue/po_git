from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NewMessagePage(BaseAction):
    receiver= By.XPATH,'//*[@text="接收者"]'
    input_value =By.XPATH,'//*[@text="键入信息"]'
    send = By.ID,'com.android.mms:id/send_button_sms'

    def input_person(self,value):
        self.input(self.receiver,value)
    def input_values(self,value):
        self.input(self.input_value,value)
    def click_send(self):
        self.click(self.send)