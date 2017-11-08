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
    def ewanUpdate(self,driver):
        self.click_images(driver,"ewanUpdate.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'ewanUpdate.1920x1080.png',way_name='channel'):
            log.info('更新提示关闭')
            return 'ok'
        else:
            return None  
    
    def login(self, driver):
        u'''渠道login'''
        #self.click_images(driver,u"idInput.1920x1080.png",way_name='channel')
        #sleep(1)
        #driver.type("Ewan10000") 
        #self.click_images(driver,u"pswInput.1920x1080.png",way_name='channel')
        #sleep(1)
        #driver.type("123456")
        if self.images_or_none(driver, 'login.1920x1080.png',way_name='channel'):
            self.click_images(driver,u"login.1920x1080.png",way_name='channel')
            image = self.images_or_none(driver, 'login_success.1920x1080.png',timeout=30)
            if image:
                log.info('登录成功')
                return 'ok'
            else:
                log.info('登录失败')
                return None
            
    def fubiao(self,driver):
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_02.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_03.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_05.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_06.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_06.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'fubiao_06.1920x1080.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None 
              

    def ali(self,driver):
        u"支付宝支付"
        self.click_images(driver,"ewan_pay_yes.1920x1080.png",way_name='channel')
        self.click_images(driver,"aliBack.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_exit_yes.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'ali_exit_yes.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
        
    def exitGame(self,driver):
        self.click_exists(driver,"setting.1920x1080.png",way_name='channel')
        self.click_exists(driver,"exitGame.1920x1080.png",way_name='channel')
        self.click_exists(driver,"exitGame_01.1920x1080.png",way_name='channel')
        self.click_exists(driver,"exitGame_02.1920x1080.png",way_name='channel')
        self.click_exists(driver,"exitGame.1920x1080.png",way_name='channel')
        self.click_exists(driver,"exitGame_01.1920x1080.png",way_name='channel')
        self.click_exists(driver,"exitGame_03.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'exitGame_03.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None
            

        


