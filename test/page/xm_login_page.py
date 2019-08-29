from selenium.webdriver.common.by import By
from test.common.page import Page

class XmLoginPage(Page):
	loc_login_username = (By.ID, 'user_name')
    loc_login_password = (By.ID, 'pwd')
    loc_login_but = (By.ID, 'login')

    def login(self, username, password):
        """登录操作"""
        self.find_element(*self.loc_login_username).send_keys(username)
        self.find_element(*self.loc_login_password).send_keys(password)
        self.find_element(*self.loc_login_but).click()
