# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'exist_02.1920x1080.png',way_name='channel'):
            self.click_images(driver,"exist_id.1920x1080.png",way_name='channel')
            sleep(1)
            self.click_images(driver,"idInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("15202828543") 
            self.click_images(driver,"pswInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("menglong")
            self.click_images(driver,"login.1920x1080.png",way_name='channel')
            self.click_images(driver,"login_shiming_close.1920x1080.png",way_name='channel')
        else:
            self.click_images(driver,"login_shiming_close.1920x1080.png",way_name='channel')
            log.info('自动登录成功')
        if self.wait_gone_images(driver,"login_shiming_close.1920x1080.png",way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None


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
        self.click_images(driver,"change_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_pay_exit.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
        
    def unionPay(self,driver): 
        u"银联卡支付"
        self.click_images(driver,"change_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"unionPay.1920x1080.png",way_name='channel')
        self.click_images(driver,"unionPay_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"unionPay_pay_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"unionPay_pay_back_yes.1920x1080.png",way_name='channel')
            
    def phonePay(self,driver): 
        u"手机支付"
        self.click_images(driver,"change_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"phonePay.1920x1080.png",way_name='channel')
        self.click_images(driver,"phonePay_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"wangdoujia_pay_back.1920x1080.png",way_name='channel')
