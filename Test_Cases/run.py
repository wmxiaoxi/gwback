
from Test_Cases.news_add_test1 import *
from Test_Cases.login_test import TestLogin
from HTMLTestRunner import HTMLTestRunner
from datetime  import date
import unittest
from BeautifulReport import BeautifulReport
# now = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
#这个方法适用于执行少量测试用例，需要手动一个一个addTest去加载，
# 如果一个类下面有很多测试用例会比较麻烦，这时候我们需要makeSuite()方法，下一篇我们接着讲
# suite.addTest(unittest.makeSuite(TestLogin))  # 一次记载多个用例
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestLogin('test_success'))
    suite.addTest(TestNews_add('test_success_add'))
    filename = '../result/htmlreport'+str(date.today())+'.html'
    ftp =  open(filename, 'wb')
    runner=HTMLTestRunner(stream=ftp,title='test report',description='report')
    #runner = unittest.TextTestRunner()
    runner.run(suite)
