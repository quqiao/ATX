#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Game(public.Methods):
    def game_update(self,driver):
        sleep(10)
        driver.click(500,500)
        sleep(5)
        driver.click(500,500)
        self.click_images(driver,"game_update_01.1920x1080.png")
        self.click_images(driver,"game_update_02.1920x1080.png")
        self.click_images(driver,"game_update_01.1920x1080.png")
        sleep(10)
        driver.click(0.5,0.5)
        self.click_images(driver,"game_update_03.1920x1080.png")
        if self.wait_gone_images(driver,'game_update_02.1920x1080.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
        
    def game_pre(self,driver):
        self.click_images(driver,"game_pre_01.1920x1080.png")
        if self.wait_gone_images(driver,'game_update_01.1920x1080.png'):
            log.info('进入游戏前准备成功')
            return 'ok'
        else:
            log.info('进入游戏前准备失败')
            return None
        
    def guide(self,driver):
        '''创建人物'''
        sleep(3)
        if self.images_or_none(driver,"guide_001.1920x1080.png"):
            self.click_images(driver,"guide_001.1920x1080.png")
            self.click_images(driver,"guide_002.1920x1080.png")
            sleep(10)
            self.click_images(driver,"guide_003.1920x1080.png")
            self.click_images(driver,"guide_004.1920x1080.png")
            '''教学'''
            self.long_click_images(driver,"guide_005.1920x1080.png")
            for i in range(200):
                driver.click(1645,926)
            for i in range(10): 
                driver.click(1770,720)#第一特殊技能
            for i in range(300):
                driver.click(1645,926)
            self.click_images(driver,"guide_008.1920x1080.png")
            self.click_images(driver,"guide_009.1920x1080.png")
            self.click_images(driver,"guide_010.1920x1080.png")
            for i in range(220):
                driver.click(1645,926)
            '''战斗2'''
            for i in range(30):
                driver.click(1645,926)
            self.click_images(driver,"guide_012.1920x1080.png")
            for i in range(360):
                driver.click(1645,926)
            self.click_images(driver,"guide_013.1920x1080.png")
            self.click_images(driver,"guide_014.1920x1080.png")
            driver.click(1645,926)
            for i in range(220):
                driver.click(1645,926)
            #self.click_images(driver,"guide_011.1920x1080.png")
            '''战斗3'''
            for i in range(20):
                driver.click(1645,926)
            self.click_images(driver,"guide_015.1920x1080.png")
            for i in range(50):
                driver.click(1645,926)
            for i in range(30):
                driver.click(530,964)
                driver.click(530,964)
                for i in range(30):
                    driver.click(1645,926)
                driver.click(110,964)
                driver.click(110,964)
                for i in range(30):
                    driver.click(1645,926)
            
            '''战斗4'''
            for i in range(50):
                driver.click(1645,926)
            
            driver.click(530,964)
            driver.click(530,964)
            for i in range(6):
                driver.click(530,964)
                driver.click(530,964)
                for i in range(30):
                    driver.click(1645,926)
                driver.click(110,964)
                driver.click(110,964)
                for i in range(30):
                    driver.click(1645,926)
            
            '''合成英雄'''
            self.click_images(driver,"guide_016.1920x1080.png")
            self.click_images(driver,"guide_017.1920x1080.png")
            self.click_images(driver,"guide_018.1920x1080.png")
            driver.click(0.5,0.5)
            driver.click(0.5,0.5)
            self.click_images(driver,"guide_019.1920x1080.png")
            
            '''故事剧情'''
            self.click_images(driver,"guide_020.1920x1080.png")
            self.click_images(driver,"guide_021.1920x1080.png")
            self.click_images(driver,"guide_022.1920x1080.png")
            self.click_images(driver,"guide_023.1920x1080.png")
            '''战斗1-1'''
            sleep(5)
            for i in range(50):
                driver.click(1645,926)
            self.click_images(driver,"guide_024.1920x1080.png")
            sleep(1)
            driver.click(0.5,0.5)
            sleep(1)
            driver.click(0.5,0.5)
            
            self.click_images(driver,"guide_025.1920x1080.png")
            for i in range(6):
                driver.click(530,964)
                driver.click(530,964)
                sleep(1)
                driver.click(530,964)
                driver.click(530,964)
                for i in range(30):
                    driver.click(1645,926)
                driver.click(110,964)
                driver.click(110,964)
                driver.click(110,964)
                driver.click(110,964)
                for i in range(30):
                    driver.click(1645,926)
            
            self.click_images(driver,"guide_026.1920x1080.png")
            for i in range(6):
                driver.click(530,964)
                driver.click(530,964)
                sleep(1)
                for i in range(30):
                    driver.click(1645,926)  
                driver.click(530,964)
                driver.click(530,964)
                sleep(1)
                for i in range(30):
                    driver.click(1645,926)  
                driver.click(530,964)
                driver.click(530,964)
                for i in range(30):
                    driver.click(1645,926)
                driver.click(110,964)
                driver.click(110,964)
                sleep(1 )
                for i in range(30):
                    driver.click(1645,926)  
                driver.click(110,964)
                driver.click(110,964)
                for i in range(30):
                    driver.click(1645,926)  
              
            '''酒馆'''
            self.click_images(driver,"guide_027.1920x1080.png")
            sleep(5)
            self.click_images(driver,"guide_028.1920x1080.png")
            self.click_images(driver,"guide_029.1920x1080.png")
            sleep(1)
            driver.click(0.5,0.5)
            sleep(1)
            driver.click(0.5,0.5)
            self.click_images(driver,"guide_030.1920x1080.png")
            for i in range(5):
                sleep(1)
                driver.click(0.5,0.5)
            sleep(3)
            driver.click(860,910)
            sleep(1)
            driver.click(860,910)
            #self.click_images(driver,"guide_031.1920x1080.png") 
            self.click_images(driver,"guide_032.1920x1080.png")
            self.click_images(driver,"guide_033.1920x1080.png")
            for i in range(2):
                sleep(1)
                driver.click(0.5,0.5) 
            self.click_images(driver,"guide_033.1920x1080.png")
        else:
            print '没有引导'
            driver.click(100,400)
            sleep(3)
            driver.click(100,400)
            
        if self.wait_gone_images(driver,'guide_033.1920x1080.png'):
            log.info('游戏引导结束')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
        
        
                
            
        
        
        