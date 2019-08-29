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
from srcut.config import Config, DATA_PATH, REPORT_PATH
from srcut.log import logger
from srcut.file_reader import ExcelReader
from srcut.HTMLTestRunner import HTMLTestRunner
#from srcut.test_youj import Email
from test.page.xm_home_page import XmHomePage

class TestXm(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/test.xlsx'

    def sub_setUp(self):
        # 初始页面是main page，传入浏览器类型打开浏览器
        self.page = XmHomePage(browser_type='chrome').get(self.URL, maximize_window=False)

    def sub_tearDown(self):
        self.page.quit()

    def test_login(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.search(d['xxxx'])
                time.sleep(2)
                self.page = XmLoginPage(self.page)  # 页面跳转到result page
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()


if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='测试网 mcf', description='修改html报告')
        runner.run(TestBaiDu('test_search'))
    # e = Email(title='测试网测试报告',
    #           message='这是今天的测试报告，请查收！',
    #           receiver='422703409@qq.com',
    #           server='...',
    #           sender='...',
    #           password='...',
    #           path=report
    #           )
    # e.send()
