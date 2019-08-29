from selenium.webdriver.common.by import By
from test.page.xm_home_page import XmUserHomePage


class XmUserHomePage(XmUserHomePage):
    loc_userhome_links = (By.XPATH, '//*[@id="top-nav"]/div/div/ul[2]/li[1]/a')

    @property
    def result_links(self):
        return self.find_elements(*self.loc_userhome_links)
