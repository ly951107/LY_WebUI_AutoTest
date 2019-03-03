from testsuites.base_testcase import BaseTestcase
from pageobjects.HomePage1 import testDiscuz1
from pageobjects.HomePage4 import testDiscuz4
import unittest
import time
from framework.logger import Logger
logger=Logger(logger="DiscuzTest4").getlog()
class DiscuzTest4(BaseTestcase):
    def test_discuz4(self):
        login6=testDiscuz1(self.driver)
        login6.adminlogin("lxc","lxc960301.")
        time.sleep(1)
        login6.defaultModule()
        time.sleep(1)
        login7=testDiscuz4(self.driver)
        login7.EditTieZi("num","one","two")
        login7.voteTieZi()




