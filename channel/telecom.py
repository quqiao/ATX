# coding=utf-8


from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'idInput.1920x1080.png',way_name='channel'):
            self.click_images(driver,"idInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("17713623912") 
            self.click_images(driver,"pswInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("test123")
            self.click_images(driver,"login.1920x1080.png",way_name='channel')
            image = self.images_or_none(driver, 'login_success.1920x1080.png',timeout=30)
            if image:
                log.info('登录成功')
                return 'ok'
            else:
                log.info('登录失败')
                return None
        elif self.images_or_none(driver, 'login_exit_id.1920x1080.png',way_name='channel'):
            self.click_images(driver,"login_exit_id.1920x1080.png",way_name='channel')
            image = self.images_or_none(driver, 'login_success.1920x1080.png',timeout=30)
            if image:
                log.info('登录成功')
                return 'ok'
            
        else:
            image = self.images_or_none(driver, 'login_success.1920x1080.png',timeout=30)
            if image:
                log.info('自动登录成功')
                return 'ok'
              

    def ali(self,driver):
        u"支付宝支付"
        self.click_images(driver,"ali.1920x1080.png",way_name='channel')
        self.click_images(driver,"aliBack.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_exit_yes.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
        
    def wechat(self,driver):
        u"微信支付"
        self.click_images(driver,"wechat.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_Back.1920x1080.png",way_name='channel')
        sleep(2)
        self.click_images(driver,"telecom_pay_close.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_02.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def telecomPay(self,driver): 
        u"翼支付"
        self.click_images(driver,"telecomPay.1920x1080.png",way_name='channel')
        self.click_images(driver,"telecomPay_cancel.1920x1080.png",way_name='channel')
        self.click_images(driver,"telecom_close.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
        
    def exitGame(self,driver):
        # self.click_images(driver,"setting.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_01.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_02.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_03.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        self.click_images(driver,"exitGame_04.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'exitGame_04.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None
    

            

