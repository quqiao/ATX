# coding=utf-8


#import os
#import unittest
#import atx
from time import sleep, strftime
import public.methods as public
#import configure
from public import logutils
log = logutils.getLogger(__name__) 

class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'idInput.1920x1080.png',way_name='channel'):
            self.click_images(driver,u"idInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("18583238812") 
            self.click_images(driver,u"pswInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("qatest123")
            self.click_images(driver,u"login.1920x1080.png",way_name='channel')
        else:
            print '自动登录'
        if self.wait_gone_images(driver, 'login.1920x1080.png',way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None
    def fubiao(self,driver):
        print ''

    def ali(self,driver):
        u"支付宝支付"
        self.click_images(driver,"ali.1920x1080.png",way_name='channel')
        self.click_images(driver,"aliBack.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_exit_yes.1920x1080.png",way_name='channel')
        self.click_images(driver,"baidu_pay_return_game.1920x1080.png",way_name='channel')
            
    
        
    def wechat(self,driver):
        u"微信支付"
        self.click_images(driver,"wechat.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_Back.1920x1080.png",way_name='channel')
        self.click_images(driver,"baidu_pay_return_game.1920x1080.png",way_name='channel')
        
    def QQ(self,driver): 
        u"银行卡支付"
        self.click_images(driver,"QQ.1920x1080.png",way_name='channel')
        sleep(3)
        driver.keyevent('BACK')
        self.click_images(driver,"baidu_pay_return_game.1920x1080.png",way_name='channel')
    

            
