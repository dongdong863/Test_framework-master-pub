import sys
#print(sys.path)
import os
#获取项目路径下的目录
os.chdir('D:\\Test_framework-master')
#打印出项目路径下的目录
#for file in os.listdir(os.getcwd()):
#    print(file)
sys.path.append('D:\\Test_framework-master')

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from srcut.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH
print("path")
from srcut.log import logger
from srcut.file_reader import ExcelReader
from srcut.HTMLTestRunner import HTMLTestRunner


class TestXm(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/test.xlsx'
    
    locator_logbut = (By.XPATH, '//*[@id="page-container"]/div[1]/div/div/div[2]/div/ul/li[7]/div/a[1]')
    locator_loginuser = (By.ID, 'user_name')
    locator_loginpaw = (By.ID, 'pwd')
    locator_login = (By.ID, 'login')
    locator_userhome = (By.XPATH, '//*[@id="page-container"]/div[1]/div/div/div[2]/div/ul/li[7]/div/a[1]')
    
    def sub_setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def sub_tearDown(self):
        self.driver.quit()


    def test_login(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.driver.find_element(*self.locator_logbut).click() #打开登录页面
                self.driver.find_element(*self.locator_loginuser).send_keys(d['username'])
                self.driver.find_element(*self.locator_loginpaw).send_keys(d['password'])
                self.driver.find_element(*self.locator_login).click()

                time.sleep(10)

                links = self.driver.find_elements(*self.locator_userhome)
                logger.info(links)
                self.sub_tearDown()


   
if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    description = 'html报告'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='测试网 mcf', description='测试报告')
        runner.run(TestXm('test_login'))



