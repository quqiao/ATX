#!/usr/bin/env python
# coding=utf-8
import os
import unittest
import atx
from time import sleep, strftime
import public.methods as public
import configure
from public import logutils
log = logutils.getLogger(__name__)
####################
"""
channel_pay_activity = u'com.flamingo.sdk.view.PluginActivity'
channel_login_activity = u'com.flamingo.sdk.view.PluginActivity'
channel_announcement_activity = u'com.game2345.account.floating.EventActivity'
wechat = u'com.tencent.mm'
alipay =u'com.alipay.sdk.app.H5PayActivity'
unionpay = u'com.unionpay.uppay.PayActivity'
guopanpay= u'com.flamingo.sdk.view.PluginActivity'
"""
#####################
class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'idInput.1920x1080.png',way_name='channel'):
        #self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,u"idInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("17713623912") 
            self.click_images(driver,u"pswInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("test123")
            self.click_images(driver,u"login.1920x1080.png",way_name='channel')
            image = self.images_or_none(driver, 'login_success.1920x1080.png')
            if image:
                log.info('登录成功')
                return 'ok'
            else:
                log.info('登录失败')
                return None
        
        elif self.images_or_none(driver, 'loginid_exit.1920x1080.png',way_name='channel'):
            self.click_images(driver,"login.1920x1080.png",way_name='channel')
            image = self.images_or_none(driver, 'login_success.1920x1080.png')
            if image:
                log.info('自动登录成功')
                return 'ok'

        else:
            image = self.images_or_none(driver, 'login_success.1920x1080.png')
            if image:
                log.info('自动登录成功')
                return 'ok'
            
    def fubiao(self,driver):
        self.click_exists(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_02.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_03.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_04.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_03.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_05.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_03.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_06.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_03.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_07.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_03.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_08.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_09.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'fubiao_09.1920x1080.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None 

    def ali(self,driver):
        u'支付宝支付'
        self.click_images(driver,"ali.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_pay_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_pay_back_yes.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None

    def wechat(self,driver):
        u'微信支付'
        self.click_images(driver,"wechat.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_back.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None


    def guopan(self,driver):
        u'''果盘支付'''
        self.click_images(driver,"guopan.1920x1080.png",way_name='channel')
        self.click_images(driver,"guopan_pay_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"guopan_pay_back_close.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_02.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
        
    def exitGame(self,driver):
        self.click_exists(driver,"setting.1920x1080.png",way_name='channel')
        self.click_exists(driver,"exitGame.1920x1080.png",way_name='channel')
        self.click_exists(driver,"exitGame_01.1920x1080.png",way_name='channel')
        self.click_exists(driver,"exitGame.1920x1080.png",way_name='channel')
        self.click_exists(driver,"exitGame_02.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'exitGame_02.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None

