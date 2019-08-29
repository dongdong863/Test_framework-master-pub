from selenium.webdriver.common.by import By
from test.common.page import Page

class XmHomePage(page):

	loc_home_loginbut = (By.XPATH, '//*[@id="page-container"]/div[1]/div/div/div[2]/div/ul/li[7]/div/a[1]')

	def loginhome(self):
        """登录页面"""
        self.find_element(*self.loc_home_loginbut).click()