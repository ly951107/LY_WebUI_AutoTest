from testsuites.base_testcase import BaseTestcase
from pageobjects.HomePage1 import testDiscuz1
from pageobjects.HomePage2 import testDiscuz2
import unittest
import time
from framework.logger import Logger
logger=Logger(logger="DiscuzTest2").getlog()
class DiscuzTest2(BaseTestcase):
     def test_discuz2(self):
        #管理员登录删帖及在管理中心建新的版块
        login2= testDiscuz2(self.driver)
        time.sleep(1)
        login2.GLlogin("admin","ly951107")           #管理员登录
        login2.Delete()
        time.sleep(3)
        login2.build("ly951107")                      #进管理中心建立新模块（密码，板块名字）
        time.sleep(10)
        login3 = testDiscuz1(self.driver)
        login3.adminlogin("lxc", "lxc960301.")  # 用户登录
        login3.newModule()
        login3.faTie("12341234", "向前走向前走")  # 发帖标题及内容

    #普通用户登录
     # def test_discuz21(self):



if __name__=="__main__":
    unittest.main()