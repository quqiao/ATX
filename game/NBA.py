#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Game(public.Methods):
    def game_update(self,driver):
        sleep(10)
        self.click_images(driver,"game_update_01.1920x1080.png")
        sleep(30)
        driver.click(0.5,0.5)
        sleep(2)
        driver.click(0.5,0.5)
        self.click_images(driver,"game_update_02.1920x1080.png") 
        sleep(2)
        driver.swipe(500,439,800,439,50)
        self.click_images(driver,"game_update_03.1920x1080.png")
        self.click_images(driver,"game_update_04.1920x1080.png")
        if self.wait_gone_images(driver,'game_update_04.1920x1080.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
        
    def game_pre(self,driver):
        self.click_images(driver,"game_pre_01.1920x1080.png")
        if self.wait_gone_images(driver,'game_pre_01.1920x1080.png'):
            log.info('进入游戏前准备成功')
            return 'ok'
        else:
            log.info('进入游戏前准备失败')
            return None
        
    def guide(self,driver):
        '''引导'''
        if self.images_or_none(driver,'guide_001.1920x1080.png'):
            '''教程-运球'''
            self.click_images(driver,"guide_001.1920x1080.png")
            sleep(8)
            self.images_or_none(driver,"guide_002.1920x1080.png")
            driver.click(500,500)    #点击任意继续
            sleep(1)
            driver.swipe(234,895,350,925,60)    #长按移动
            sleep(1)
            driver.swipe(234,895,340,838,70)    #长按移动
            '''教程-投篮'''
            sleep(5)
            driver.click(500,500)    #点击任意继续
            sleep(1)
            driver.swipe(1746,710,1746,710,20)    #长按跳投
            '''教程-三分投篮'''
            sleep(6)
            driver.click(500,500)    #点击任意继续
            sleep(3)
            driver.swipe(234,895,330,924,40)    #长按移动
            sleep(2)
            driver.swipe(1746,710,1746,710,20)    #长按跳投
            '''教程-如何冲刺'''
            sleep(6)
            driver.click(500,500)    #点击任意继续
            sleep(3)
            driver.swipe(1746,920,1746,920,300)    #长按冲刺
            '''教程-如何灌篮'''
            sleep(6)
            driver.click(500,500)    #点击任意继续
            sleep(3)
            driver.swipe(1746,920,1746,920,30)   #长按冲刺
            driver.swipe(1746,920,1746,680,30)    #灌篮
            '''教程-教程结束'''
            sleep(6)
            driver.click(500,500)    #点击任意继续
            sleep(3)
            driver.swipe(1746,920,1746,920,30)   #长按冲刺
            driver.swipe(1746,920,1746,680,30)    #灌篮
            '''教程结果'''
            self.click_images(driver,"guide_003.1920x1080.png")
            '''组建球队'''
            self.click_images(driver,"guide_004.1920x1080.png")
            self.click_images(driver,"guide_005.1920x1080.png")
            sleep(1)
            driver.type('wedfg')
            sleep(1)
            driver.click(100,100)
            self.click_images(driver,"guide_003.1920x1080.png")
            self.click_images(driver,"guide_006.1920x1080.png")
            self.click_images(driver,"guide_007.1920x1080.png")
            '''商店'''
            self.click_images(driver,"guide_008.1920x1080.png")
            self.click_images(driver,"guide_009.1920x1080.png")
            self.click_images(driver,"guide_010.1920x1080.png")
            self.click_images(driver,"guide_011.1920x1080.png")
            '''升级球队'''
            self.click_images(driver,"guide_012.1920x1080.png")
            self.click_images(driver,"guide_013.1920x1080.png")
            self.click_images(driver,"guide_014.1920x1080.png")
            sleep(3)
            driver.click(629,450)#可升级球员
            self.click_images(driver,"guide_015.1920x1080.png")
            self.click_images(driver,"guide_016.1920x1080.png")
            self.click_images(driver,"guide_017.1920x1080.png")
            self.click_images(driver,"guide_018.1920x1080.png")
            self.click_images(driver,"guide_019.1920x1080.png")
            sleep(5)
            driver.click(500,500)
            '''在线赛事'''
            self.click_images(driver,"guide_020.1920x1080.png")
        else:
            print '引导已过'
        if self.wait_gone_images(driver,'guide_020.1920x1080.png'):
            log.info('引导成功')
            return 'ok'
        else:
            log.info('引导失败')
            return None