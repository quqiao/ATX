# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'login_01.1920x1080.png',way_name='channel'):
            sleep(1)
            driver.click(665,643)  # QQ登录
            sleep(6)
            driver.click(580,1720)  # 登录
            sleep(2)
            driver.click(1720,70)  # 关闭实名注册
            log.info('QQ登录')
            # self.click_images(driver,"idInput.1920x1080.png",way_name='channel')
            # sleep(1)
            # driver.type("yzrtest7")
            # self.click_images(driver,"pswInput.1920x1080.png",way_name='channel')
            # sleep(1)
            # driver.type("123456")
            # self.click_images(driver,"login.1920x1080.png",way_name='channel')
            # self.click_images(driver,"login_bangdingshouji.1920x1080.png",way_name='channel')
        else:
            sleep(1)
            driver.click(960,690)  # 直接登录
            sleep(5)
            driver.click(1720,70)  # 关闭实名注册
            log.info('直接登录')
        if self.wait_gone_images(driver,"login_01.1920x1080.png",way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None

    def fubiao(self,driver):
        log.info('该渠道没有浮标操作')
        if self.wait_gone_images(driver,"login_01.1920x1080.png",way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None
              

    def ali(self,driver):
        u"支付宝支付"
        
        self.click_images(driver,"guanfang_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_pay_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_pay_back_yes.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None 
            
    def wechat(self,driver):
        u"微信支付"
        
        self.click_images(driver,"wechat.1920x1080.png",way_name='channel')
        self.click_images(driver,"guanfang_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_back_cancel.1920x1080.png",way_name='channel')
        sleep(2)
        driver.keyevent('BACK')
        driver.keyevent('BACK')
        if self.images_or_none(driver, 'exists_02.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None 
            
    # def youyuwan(self,driver):
    #     u"游娱玩支付"
    #     if self.get_view_info(driver) == channel_pay_activity:
    #         self.click_images(driver,"youyuwan.1920x1080.png",way_name='channel')
    #         self.click_images(driver,"guanfang_pay.1920x1080.png",way_name='channel')
    #         self.click_images(driver,"youyuwan_pay_back.1920x1080.png",way_name='channel')
    #         self.click_images(driver,"youyuwan_pay_back_yes.1920x1080.png",way_name='channel')
            
            
    # def phonePay(self,driver):
    #     u"充值卡支付"
    #     if self.get_view_info(driver) == channel_pay_activity:
    #         self.click_images(driver,"phonePay.1920x1080.png",way_name='channel')
    #         self.click_images(driver,"guanfang_pay.1920x1080.png",way_name='channel')
    #         self.click_images(driver,"yingyongdou_pay_back_yes.1920x1080.png",way_name='channel')
            

            
    def exitGame(self,driver):
        # self.click_images(driver,"setting.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_01.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_02.1920x1080.png",way_name='channel')
        log.info('该渠道没有退出游戏')
        if self.wait_gone_images(driver, 'login_01.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None




            



