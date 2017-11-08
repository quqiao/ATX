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
channel_login_activity = u'com.qihoo.gamecenter.sdk.activity.ContainerActivity'
channel_pay_activity = u'com.baidu.platformsdk.CashierDeskActivity'
channel_announcement_activity = u'com.game2345.account.floating.EventActivity'
wechat = u'com.tencent.mm'
alipay =u'com.alipay.sdk.app.H5PayActivity'
unionpay = u'com.unionpay.uppay.PayActivity'
#####################

class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.get_view_info(driver) == channel_login_activity:
                self.click_images(driver,"idInput.1920x1080.png",way_name='channel')
                sleep(1)
                driver.type("17713623912") 
                self.click_images(driver,"pswInput.1920x1080.png",way_name='channel')
                sleep(1)
                driver.type("test123")
                self.click_images(driver,"login.1920x1080.png",way_name='channel')
                self.click_images(driver,"login_shimingzhi_close.1920x1080.png",way_name='channel')
                image = self.wait_gone_images(driver, 'login_shimingzhi_close.1920x1080.png',way_name='channel')
                if image:
                    log.info('登录成功')
                    return 'ok'
                else:
                    log.info('登录失败')
                    return None

        else:
            self.click_images(driver,"login_shimingzhi_close.1920x1080.png",way_name='channel')
            image = self.wait_gone_images(driver, 'login_shimingzhi_close.1920x1080.png',way_name='channel')
            if image:
                log.info('自动登录成功')
                return 'ok'
              
    def fubiao(self,driver):
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_02.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_03.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_05.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_06.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_07.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_08.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_09.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_10.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'fubiao_10.1920x1080.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None 
        
    def ali(self,driver):
        u"支付宝支付"
        #if self.get_view_info(driver) == channel_pay_activity:
        self.click_images(driver,"ali.1920x1080.png",way_name='channel')
        self.click_images(driver,"anzhi_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_pay_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_pay_back_yes.1920x1080.png",way_name='channel')
        self.click_images(driver,"anzhi_pay_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"anzhi_pay_back_yes.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None 
            
    def wechat(self,driver):
        u"微信支付"
        #if self.get_view_info(driver) == channel_pay_activity:
        self.click_images(driver,"wechat.1920x1080.png",way_name='channel')
        self.click_images(driver,"anzhi_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_back_cancel.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_02.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None 
    '''        
    def UnionPay(self,driver):
        u"银联支付"
        #if self.get_view_info(driver) == channel_pay_activity:
        self.click_images(driver,"UnionPay.1920x1080.png",way_name='channel')
        self.click_images(driver,"anzhi_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"UnionPay_back.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_04.1920x1080.png'):
            return 'ok'
        else:
            return None 
    '''
            
    """
    def VISAPay(self,driver):
        u"银联支付"
        if self.get_view_info(driver) == channel_pay_activity:
            self.click_images(driver,"muzhihui_changge_pay.1920x1080.png",way_name='channel')
            self.click_images(driver,"VISA.1920x1080.png",way_name='channel')
            self.click_images(driver,"muzhihui_pay.1920x1080.png",way_name='channel')
            self.click_images(driver,"UnionPay_back.1920x1080.png",way_name='channel')
    """
            
    def phonePay(self,driver):
        u"手机点卡支付"
        #if self.get_view_info(driver) == channel_pay_activity:
        self.click_images(driver,"anzhi_pay_changepay.1920x1080.png",way_name='channel')
        self.click_images(driver,"phonePay.1920x1080.png",way_name='channel')
        self.click_images(driver,"anzhi_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"phonePay_back.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_04.1920x1080.png'):
            return 'ok'
        else:
            return None
        
    def exitGame(self,driver):
        self.click_images(driver,"setting.1920x1080.png",way_name='channel')
        self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        self.click_images(driver,"exitGame_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        self.click_images(driver,"exitGame_02.1920x1080.png",way_name='channel')
        self.click_images(driver,"exitGame_03.1920x1080.png",way_name='channel')
        self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        self.click_images(driver,"exitGame_04.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'exitGame_04.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None
        
        
        
        
            
    