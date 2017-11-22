#!/usr/bin/env python
# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'login_01.1920x1080.png',way_name='channel'):
            # self.click_images(driver,u"idInput.1920x1080.png",way_name='channel')
            # sleep(1)
            # driver.type("15198139230")
            # self.click_images(driver,u"pswInput.1920x1080.png",way_name='channel')
            # sleep(1)
            # driver.type("a123123")
            # self.click_images(driver,u"login.1920x1080.png",way_name='channel')
            # self.click_images(driver,u"login_shiming_returnGame.1920x1080.png",way_name='channel')
            sleep(2)
            driver.click(860,469)  # 点击账号输入框
            sleep(1)
            driver.clear_text()
            sleep(2)
            driver.type("15198139230",next=True)
            sleep(2)
            driver.type("a123123")
            sleep(2)
            driver.click(900,850)  # 登录按钮
            sleep(3)
            driver.click(1368,119)  # 返回游戏
        else:
            sleep(3)
            driver.click(1368,119)  # 返回游戏
        if self.wait_gone_images(driver, 'login_shiming_returnGame.1920x1080.png',way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None
            
    def fubiao(self,driver):
        self.click_exists(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_02.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_03.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_04.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_03.1920x1080.png",way_name='channel')
        
        
        
        

    def ali(self,driver):
        self.click_images(driver,"ali.1920x1080.png",way_name='channel')    
        self.click_images(driver,"ali_pay_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_pay_back_yes.1920x1080.png",way_name='channel')
        sleep(1)
        driver.keyevent('BACK')
        if self.images_or_none(driver, 'exists_01.1920x1080.png'):
            return 'ok'
        else:
            return None 

    def phonePay(self,driver):
        self.click_images(driver,"phonePay.1920x1080.png",way_name='channel')
        sleep(2) 
        driver.keyevent('BACK')
        sleep(2)
        driver.keyevent('BACK')
        if self.images_or_none(driver, 'exists_01.1920x1080.png'):
            return 'ok'
        else:
            return None 

    def exitGame(self,driver):
        log.info('该游戏没有渠道退出')
        if self.wait_gone_images(driver, 'exitGame_02.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
    


