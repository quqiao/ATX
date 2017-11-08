# coding=utf-8

#import os
#import unittest
#import atx
from time import sleep, strftime
import public.methods as public
#import configure
from public import logutils
log = logutils.getLogger(__name__)

####################
channel_shiming_activity = u'com.qihoo.gamecenter.sdk.activity.ContainerActivity'
channel_pay_activity = u'com.baidu.platformsdk.CashierDeskActivity'
channel_announcement_activity = u'com.game2345.account.floating.EventActivity'
wechat = u'com.tencent.mm'
alipay =u'com.alipay.sdk.app.H5PayActivity'
unionpay = u'com.unionpay.uppay.PayActivity'
#####################

class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, u'yingyonghui_change_login.1920x1080.png',way_name='channel'):
            self.click_images(driver,u"yingyonghui_change_login.1920x1080.png",way_name='channel')
            self.click_images(driver,u"idInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("15198139230") 
            self.click_images(driver,u"pswInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("a123123")
            self.click_images(driver,u"login.1920x1080.png",way_name='channel')
            image = self.images_or_none(driver, 'login_success.1920x1080.png')
            if image:
                log.info('登录成功')
                return 'ok'
            else:
                log.info('登录失败')
                return None
        else:
            image = self.images_or_none(driver, 'login_success.1920x1080.png')
            if image:
                log.info('自动登录成功')
                return 'ok'
              

    def ali(self,driver):
        u"支付宝支付"
        self.click_images(driver,"pay_shiming_close.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_pay_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_pay_back_yes.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def wechat(self,driver):
        u"微信支付"
        self.click_images(driver,"wechat.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_back.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def yingyongdou(self,driver):
        u"应用豆支付"
        if self.get_view_info(driver) == channel_pay_activity:
            self.click_images(driver,"yingyongdou.1920x1080.png",way_name='channel')
            self.click_images(driver,"yingyongdou_pay_cancel.1920x1080.png",way_name='channel')
            
    def caifutong(self,driver):
        u"财付通支付"
        if self.get_view_info(driver) == channel_pay_activity:
            self.click_images(driver,"caifutong.1920x1080.png",way_name='channel')
            self.click_images(driver,"yingyongdou_pay_back.1920x1080.png",way_name='channel')
            self.click_images(driver,"yingyongdou_pay_back_yes.1920x1080.png",way_name='channel')
            
    def phonePay(self,driver):
        u"手机支付"
        if self.get_view_info(driver) == channel_pay_activity:
            self.click_images(driver,"phonePay.1920x1080.png",way_name='channel')
            self.click_images(driver,"phonePay_back.1920x1080.png",way_name='channel')

            



