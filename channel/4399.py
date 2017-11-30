# coding=utf-8
#!/usr/bin/env python



from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver,"login_01.1920x1080.png",way_name='channel'):
            # self.click_images(driver,"idInput.1920x1080.png",way_name='channel')
            # sleep(1)
            # driver.type("1682930949")
            # self.click_images(driver,"pswInput.1920x1080.png",way_name='channel')
            # sleep(1)
            # driver.type("123456")
            # self.click_images(driver,"login.1920x1080.png",way_name='channel')
            sleep(2)
            driver.click(690,270)  # 点击账号
            sleep(1)
            driver.clear_text()
            sleep(1)
            driver.type("1682930949",next=True)
            sleep(1)
            driver.type("123456")
            sleep(1)
            driver.click(900,620)  # 登录

        else:
            sleep(6)
            log.info('自动登录成功')
            return 'ok'
        if self.wait_gone_images(driver, 'login.1920x1080.png',way_name='channel',timeout=40):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None

    def fubiao(self,driver):
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_02.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_03.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_05.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_06.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_05.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_07.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_05.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_08.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_09.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_10.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_05.1920x1080.png",way_name='channel')
        self.click_images   (driver,"fubiao_11.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'fubiao_01.1920x1080.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None  

    def ali(self,driver):
        u"支付宝支付"
        self.click_images(driver,"ali.1920x1080.png",way_name='channel')
        self.click_images(driver,"4399_pay_certain.1920x1080.png",way_name='channel')
        self.click_images(driver,"aliBack.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_exit_yes.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None

    def wechat(self,driver):
        u"微信支付"
        self.click_images(driver,"wechat.1920x1080.png",way_name='channel')
        self.click_images(driver,"4399_pay_certain.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_Back.1920x1080.png",way_name='channel')
        self.click_images(driver,"4399_pay_close.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def QQ(self,driver): 
        u"QQ支付"
        if self.get_view_info(driver):
            self.click_images(driver,"exchange_pay.1920x1080.png",way_name='channel')
            self.click_images(driver,"QQ.1920x1080.png",way_name='channel')
            self.click_images(driver,"4399_pay_certain.1920x1080.png",way_name='channel')
            driver.keyenvent("BACK")
            self.click_images(driver,"4399_pay_close.1920x1080.png",way_name='channel')
            

    def caifutong(self,driver):
        u"财付通支付"
        if self.get_view_info(driver):
            self.click_images(driver,"exchange_pay.1920x1080.png",way_name='channel')
            self.click_images(driver,"caifutong.1920x1080.png",way_name='channel')
            self.click_images(driver,"4399_pay_certain.1920x1080.png",way_name='channel')
            driver.keyenvent("BACK")
            self.click_images(driver,"caifutong_exit_yes.1920x1080.png",way_name='channel')
            self.click_images(driver,"4399_pay_close.1920x1080.png",way_name='channel')
            
    def exitGame(self,driver):
        # self.click_images(driver,"setting.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_01.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_02.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_03.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_01.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_04.1920x1080.png",way_name='channel')
        sleep(2)
        driver.click(665,810)  # 退出游戏
        if self.wait_gone_images(driver, 'exitGame_04.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            log.info('退出游戏失败')
            return None


