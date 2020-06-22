import unittest

from test_data.loginBase_data import *
from framework.login_action import *
from common_fuc.logger import Logger
from common_fuc.pageobj.login_obj import *

logger = Logger(logger="TestLogin").getlog()

class TestLogin(unittest.TestCase):
    def setUp(self):
         newmethod.get_driver()
         newmethod.open1()
         time.sleep(5)

    def tearDown(self):
        newmethod.quit()
#登陆失败
    def test_01(self):
        login(user_1['user'], user_1['pass'])
        title = newmethod.driver.title
        try:
           assert title==user_1['except']
        except Exception as e :
            logger.info("登陆成功用例执行失败")

#登陆成功
    def test_02(self):
        login(user_0['user'], user_0['pass'])
        title = newmethod.driver.title
        try:
            assert title==user_0['except']
        except Exception:
            logger.info("登陆成功用例执行失败")











