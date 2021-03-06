#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)
import configure

class Game(public.Methods):
    def game_update(self,driver):
        sleep(15)
        #self.click_images(driver,"game_update_01.1920x1080.png")
        #self.driver.start_app(configure.package_name,configure.activity_name)
        if self.wait_gone_images(driver,'game_pre_02.1920x1080.png'):
            log.info('游戏更新成功')
            print "执行successful！"
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
    def game_pre(self,driver):
        sleep(5)
        #self.click_images(driver,"game_pre_01.1920x1080.png")
        sleep(10)
        self.click_images(driver,"game_pre_02.1920x1080.png")
        sleep(10)
        driver.click(0.5,0.5)
        if self.wait_gone_images(driver,'game_pre_02.1920x1080.png'):
            log.info('进入游戏前准备成功')
            return 'ok'
        else:
            log.info('进入游戏前准备失败')
            return None
    def guide(self,driver):
        """
        sleep(10)
        for i in range(5):
            driver.click(0.5,0.5)
            sleep(2)
        driver.click(963,462)
        self.click_images(driver,"guide_001.1920x1080.png")
        self.click_images(driver,"guide_002.1920x1080.png")
        sleep(5)
        driver.click(0.5,0.5)
        sleep(5)
        self.click_images(driver,"guide_003.1920x1080.png")
        for i in range(50):
            driver.long_click(1680,860)
            driver.swipe(330,750,380,750)
            driver.long_click(1680,860)
            driver.swipe(380,750,330,750)
            driver.long_click(1680,860)
            driver.swipe(330,750,280,750)
            driver.long_click(1680,860)
            driver.swipe(280,750,330,750)
            driver.long_click(1680,860)
            if self.exist(driver,"guide_004.1920x1080.png"):
                break
        
        '''开启自动射击'''
        self.click_images(driver,"guide_004.1920x1080.png")
        """
        sleep(1)
        driver.click(760,410)
        #self.click_images(driver,"guide_005.1920x1080.png")
        self.click_images(driver,"guide_006.1920x1080.png")
        '''开始战斗'''
        for i in range(100):
            driver.swipe(330,750,380,750)
            driver.swipe(380,750,330,750)
            driver.swipe(330,750,280,750)
            driver.swipe(280,750,330,750)
            if self.exist(driver,"guide_015.1920x1080.png"):
                break
        
        '''关闭对话'''
        for i in range(20):
            driver.click(0.5,0.5)
            sleep(1)
        
        '''战役模式1'''
        self.click_images(driver,"guide_007.1920x1080.png")
        self.click_images(driver,"guide_008.1920x1080.png")
        self.click_images(driver,"guide_009.1920x1080.png")
        self.click_images(driver,"guide_010.1920x1080.png")
        self.click_images(driver,"guide_011.1920x1080.png")
        for i in range(100):
            sleep(1)
            driver.click(0.5,0.5)
            driver.swipe(330,750,380,750)
            driver.swipe(380,750,330,750)
            driver.swipe(330,750,280,750)
            driver.swipe(280,750,330,750)
            if self.exist(driver,"guide_012.1920x1080.png"):
                break
        
        self.click_images(driver,"guide_012.1920x1080.png")
        
        self.click_images(driver,"guide_014.1920x1080.png")
        '''战役模式2'''
        sleep(10)
        driver.click(0.5,0.5)
        self.click_images(driver,"guide_007.1920x1080.png")
        self.click_images(driver,"guide_008.1920x1080.png")
        for i in range(100):
            driver.swipe(330,750,380,750)
            driver.swipe(380,750,330,750)
            driver.swipe(330,750,280,750)
            driver.swipe(280,750,330,750)
            if self.exist(driver,"guide_012.1920x1080.png"):
                break
        
        self.click_images(driver,"guide_012.1920x1080.png")
        self.click_images(driver,"guide_014.1920x1080.png")
        '''战役模式3'''
        sleep(10)
        for i in range(5):
            sleep(1)
            driver.click(0.5,0.5)
        self.click_images(driver,"guide_007.1920x1080.png")
        self.click_images(driver,"guide_008.1920x1080.png")
        sleep(10)
        for i in range(100):
            driver.click(0.5,0.5)
            driver.swipe(330,750,380,750)
            driver.swipe(380,750,330,750)
            driver.swipe(330,750,280,750)
            driver.swipe(280,750,330,750)
            if self.exist(driver,"guide_013.1920x1080.png"):
                break
        self.click_images(driver,"guide_013.1920x1080.png")
        for i in range(100):
            driver.click(0.5,0.5)
            driver.swipe(330,750,380,750)
            driver.swipe(380,750,330,750)
            driver.swipe(330,750,280,750)
            driver.swipe(280,750,330,750)
            if self.exist(driver,"guide_012.1920x1080.png"):
                break
        self.click_images(driver,"guide_012.1920x1080.png")
        self.click_images(driver,"guide_014.1920x1080.png")
        sleep(10)
        for i in range(3):
            sleep(1)
            driver.click(0.5,0.5)
        
        
        
        
        
