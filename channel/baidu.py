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
        if self.images_or_none(driver, 'login_01.1920x1080.png',way_name='channel'):
            driver.click(900,280)  # 点击输入框
            sleep(2)
            driver.clear_text()
            sleep(1)
            driver.type("lytest006",next=True)
            sleep(1)
            driver.type("123456Ly")
            sleep(1)
            driver.click(900,600)  # 登录
            sleep(3)
            driver.click(1459,106)  # 关闭实名
            log.info('输入账号密码登录')
            # self.click_images(driver,u"idInput.1920x1080.png",way_name='channel')
            # sleep(1)
            # driver.type("18583238812")
            # self.click_images(driver,u"pswInput.1920x1080.png",way_name='channel')
            # sleep(1)
            # driver.type("qatest123")
            # self.click_images(driver,u"login.1920x1080.png",way_name='channel')
        else:
            sleep(3)
            driver.click(1459,106)  # 关闭实名
            log.info('自动登录')
        if self.wait_gone_images(driver, 'login.1920x1080.png',way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None

    def fubiao(self, driver):
        log.info('暂时没有浮标')
        if self.wait_gone_images(driver, 'login.1920x1080.png',way_name='channel'):
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
        sleep(1)
        self.click_images(driver,"baidu_pay_return_game.1920x1080.png",way_name='channel')
    

    def exitGame(self,driver):
        sleep(1)
        driver.click(1040,720)  # 退出游戏
        sleep(2)
        if self.wait_gone_images(driver, 'login_01.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None