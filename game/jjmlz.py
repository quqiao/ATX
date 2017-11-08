#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Game(public.Methods):
    def game_update(self,driver):
        sleep(20)
        for i in range(5):
            driver.click(500,500)
            sleep(1)
        sleep(60)
        driver.click(500,500)
        sleep(60)
        self.images_or_none(driver,"game_update_01.1920x1080.png")
        driver.click(0.5,0.5)
        sleep(2)
        '''开始战斗'''
        driver.swipe(297,825,297,669,100)
        '''第一轮攻击'''
        for i in range(200):
            driver.click(1685,881)    #发动攻击
        for i in range(5):
            driver.swipe(297,825,297,669,100)
            driver.swipe(297,825,160,825,100)
        '''第二乱攻击'''
        for i in range(300):
            driver.click(1685,881)    #发动攻击
        if self.wait_gone_images(driver,'game_update_01.1920x1080.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
        
        
    def game_pre(self,driver):
        self.click_images(driver,"game_pre_01.1920x1080.png")
        self.click_images(driver,"game_pre_02.1920x1080.png")
        if self.wait_gone_images(driver,'game_pre_02.1920x1080.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
        
        
    def guide(self,driver):
        if self.images_or_none(driver,"guide_01.1920x1080.png"):
            self.click_images(driver,"guide_01.1920x1080.png")
            self.click_images(driver,"guide_02.1920x1080.png")
            self.click_images(driver,"guide_03.1920x1080.png")
            self.click_images(driver,"guide_04.1920x1080.png")
        else:
            self.click_images(driver,"guide_03.1920x1080.png")
            self.click_images(driver,"guide_04.1920x1080.png")
        if self.wait_gone_images(driver,'guide_04.1920x1080.png'):
            log.info('游戏引导成功')
            return 'ok'
        else:
            log.info('游戏引导失败')
            return None
            
        
