from selenium.webdriver.common.by import By
from pageobjects.BasePage import BasePage
import time
from framework.logger import Logger
logger=Logger(logger="testDiscuz4").getlog()
class testDiscuz4(BasePage):
    FaNewTie=(By.CSS_SELECTOR,"#newspecial")                                    #发新帖
    vote=(By.LINK_TEXT,"发起投票")                                              #发起投票
    TextKuang=(By.CSS_SELECTOR,".bm .pbt .z input")                             #输入文本标题
    text1=(By.CSS_SELECTOR,".sinf div:nth-child(4) p:nth-child(1) input")  #输入选项1
    text2=(By.CSS_SELECTOR,".sinf div:nth-child(4) p:nth-child(2) input")   #输入选项2
    voteBtn=(By.CSS_SELECTOR,".bm .mtm span")                                   #发起投票按钮
    theme=(By.CSS_SELECTOR,"#thread_subject")                                       #主题名称
    compare1=(By.CSS_SELECTOR,"#poll > div.pcht > table > tbody > tr:nth-child(2) > td:nth-child(2)")   #比例1
    compare2= (By.CSS_SELECTOR, "#poll > div.pcht > table > tbody > tr:nth-child(4) > td:nth-child(2)")     #比例2
    option_1=(By.CSS_SELECTOR,"#option_1")                                              #单选1
    option_2 = (By.CSS_SELECTOR, "#option_2")                                           #单选2
    Name1=(By.CSS_SELECTOR,"#poll > div.pcht > table > tbody > tr:nth-child(1) > td.pvt > label")                           #单选姓名1
    Name2=(By.CSS_SELECTOR,"#poll > div.pcht > table > tbody > tr:nth-child(3) > td.pvt > label")                           #单选姓名2                                                      #单选姓名2
    sumbit=(By.CSS_SELECTOR,"#pollsubmit")
    def EditTieZi(self,title,content1,content2):
        time.sleep(3)
        self.click(*self.FaNewTie)
        self.click(*self.vote)
        time.sleep(3)
        self.sendkeys(title,*self.TextKuang)
        self.sendkeys(content1,*self.text1)
        self.sendkeys(content2,*self.text2)
        time.sleep(3)
        self.click(*self.voteBtn)
    def voteTieZi(self):
        self.click(*self.option_1)
        self.click(*self.sumbit)
        # self.switch_to_iframe()
        Theme=self.HuoQuText(*self.theme)
        name1=self.HuoQuText(*self.Name1)
        Name2 = self.HuoQuText(*self.Name2)
        Compare1=self.HuoQuText(*self.compare1)
        Compare2 = self.HuoQuText(*self.compare2)
        logger.info("主题是：%s"%Theme)
        logger.info("选项1名称：%s"%name1)
        logger.info("选项1投票比例：%s"%Compare1)
        logger.info("选项2名称：%s"%Name2)
        logger.info("选项2投票比例：%s" % Compare2)



    # def PrintInfo(self):
    #     self.Print("投票的主题名称是：",*self.theme)
    #     self.Print("选项1名称：%s,选项1投票比例：%s"%(*self.Name1,*self.compare1))
    #     self.Print("选项1名称：%s,选项1投票比例：%s" % (*self.Name2, *self.compare2))




