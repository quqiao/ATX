#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Game(public.Methods):
    
    def game_update(self,driver):
        sleep(30)
        driver.click(500,500)
        sleep(20)
        self.click_images(driver,"game_update_01.1920x1080.png")
        if self.wait_gone_images(driver,'game_update_01.1920x1080.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
    
    def game_pre(self,driver):
        self.click_images(driver,"game_pre_01.1920x1080.png")
        sleep(10)
        self.images_or_none(driver,'game_pre_02.1920x1080.png')
        driver.click(0.5,0.5)
        sleep(3)
        driver.click(0.5,0.5)
        sleep(3)
        driver.click(0.5,0.5)
        self.click_images(driver,"game_pre_03.1920x1080.png")
        if self.wait_gone_images(driver,'game_pre_03.1920x1080.png'):
            log.info('进入游戏前准备成功')
            return 'ok'
        else:
            log.info('进入游戏前准备失败')
            return None
        
        
    def guide(self,driver):
        '''开始引导，第一场战斗'''
        if self.images_or_none(driver,'guide_001.1920x1080.png'):
            self.click_images(driver,"guide_001.1920x1080.png")
            self.click_images(driver,"guide_002.1920x1080.png")
            for i in range(1000):
                for i in range(20):
                    driver.click(1789,950)
                if self.exist(driver,'guide_003.1920x1080.png'):
                    self.click_images(driver,"guide_004.1920x1080.png")
                    break
                    
            '''第二场战斗'''
            for i in range(1000):
                for i in range(40):
                    driver.click(1789,950)
                if self.exist(driver,'guide_006.1920x1080.png'):
                    self.click_images(driver,"guide_007.1920x1080.png")
                    break
            '''第三场战斗'''
            for i in range(1000):
                for i in range(20):
                    driver.click(1789,950)
                if self.exist(driver,'guide_008.1920x1080.png'):
                    self.click_images(driver,"guide_008.1920x1080.png")
                    break
            for i in range(1000):
                for i in range(20):
                    driver.click(1789,950)
                if self.exist(driver,'guide_009.1920x1080.png'):
                    self.click_images(driver,"guide_010.1920x1080.png")
                    break
            
            for i in range(1000):
                driver.swipe(500,682,500,300,10)
                for i in range(39):
                    driver.click(1789,950)
                if self.exist(driver,'guide_012.1920x1080.png'):
                    self.click_images(driver,"guide_011.1920x1080.png")
                    break
            '''出征'''
            driver.click(0.5,0.5)
            self.click_images(driver,"guide_011.1920x1080.png")
            self.click_images(driver,"guide_012.1920x1080.png")
            sleep(1)
            driver.click(0.5,0.5)
            sleep(1)
            driver.click(0.5,0.5)
            sleep(1)
            driver.click(0.5,0.5)
            self.click_images(driver,"guide_013.1920x1080.png")
            self.click_images(driver,"guide_014.1920x1080.png")
            self.click_images(driver,"guide_015.1920x1080.png")
            self.click_images(driver,"guide_016.1920x1080.png")
            '''第四场战斗'''
            for i in range(1000):
                for i in range(50):
                    driver.click(1789,950)
                if self.exist(driver,'guide_017.1920x1080.png'):
                    self.click_images(driver,"guide_017.1920x1080.png")
                    break
            '''装备'''
            self.click_images(driver,"guide_017.1920x1080.png")
            self.click_images(driver,"guide_018.1920x1080.png")
            self.click_images(driver,"guide_019.1920x1080.png")
            self.click_images(driver,"guide_020.1920x1080.png")
            self.click_images(driver,"guide_021.1920x1080.png")
            self.click_images(driver,"guide_022.1920x1080.png")
            self.click_images(driver,"guide_020.1920x1080.png")
            self.click_images(driver,"guide_023.1920x1080.png")
            '''颍川别战'''
            self.click_images(driver,"guide_024.1920x1080.png")
            for i in range(1000):
                for i in range(20):
                    driver.click(1789,950)
                if self.exist(driver,'guide_025.1920x1080.png'):
                    self.click_images(driver,"guide_025.1920x1080.png")
                    break
            self.click_images(driver,"guide_026.1920x1080.png")
            self.click_images(driver,"guide_027.1920x1080.png")
            self.click_images(driver,"guide_028.1920x1080.png")
            sleep(15)
            for i in range(6):
                sleep(1)
                driver.click(1789,950)
            self.click_images(driver,"guide_029.1920x1080.png")
            for i in range(1000):
                for i in range(20):
                    driver.click(1789,950)
                if self.exist(driver,'guide_030.1920x1080.png'):
                    self.click_images(driver,"guide_030.1920x1080.png")
                    break
            '''决战傀儡'''
            #self.click_images(driver,"guide_030.1920x1080.png")
            self.click_images(driver,"guide_027.1920x1080.png")
            self.click_images(driver,"guide_028.1920x1080.png")
            sleep(30)
            for i in range(1000):
                for i in range(20):
                    driver.click(1789,950)
                if self.exist(driver,'guide_031.1920x1080.png'):
                    self.click_images(driver,"guide_031.1920x1080.png")
                    break
            '''装备'''
            self.click_images(driver,"guide_031.1920x1080.png")
            self.click_images(driver,"guide_032.1920x1080.png")
            self.click_images(driver,"guide_033.1920x1080.png")
            self.click_images(driver,"guide_020.1920x1080.png")
            self.click_images(driver,"guide_023.1920x1080.png")
            self.click_images(driver,"guide_025.1920x1080.png")
            self.click_images(driver,"guide_042.1920x1080.png")
            self.click_images(driver,"guide_041.1920x1080.png")
            self.click_images(driver,"guide_026.1920x1080.png")
            self.click_images(driver,"guide_027.1920x1080.png")
            self.click_images(driver,"guide_028.1920x1080.png")
            '''羌林杀机'''
            for i in range(1000):
                driver.click(0.5,0.5)
                if self.exist(driver,'guide_005.1920x1080.png'):
                    self.click_images(driver,"guide_005.1920x1080.png")
                    break
            '''江夏之战'''
            self.click_images(driver,"guide_034.1920x1080.png")
            self.click_images(driver,"guide_027.1920x1080.png")
            self.click_images(driver,"guide_028.1920x1080.png")
            for i in range(1000):
                driver.click(0.5,0.5)
                if self.exist(driver,'guide_005.1920x1080.png'):
                    self.click_images(driver,"guide_005.1920x1080.png")
                    break
            self.click_images(driver,"guide_035.1920x1080.png")
            '''装备-一键强化'''
            self.click_images(driver,"guide_031.1920x1080.png")
            self.click_images(driver,"guide_036.1920x1080.png")
            self.click_images(driver,"guide_037.1920x1080.png")
            self.click_images(driver,"guide_038.1920x1080.png")
            self.click_images(driver,"guide_038.1920x1080.png")
            self.click_images(driver,"guide_039.1920x1080.png")
            self.click_images(driver,"guide_040.1920x1080.png")
            self.click_images(driver,"guide_020.1920x1080.png")
            self.click_images(driver,"guide_023.1920x1080.png")
        else:
            print '没有引导'
            #driver.click(500,500)
        
        if self.wait_gone_images(driver,'guide_023.1920x1080.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
            

    '''
    def basicFunction(self,driver):
        
    def live(self,driver):
        
    def gonglue(self,driver):
        
    def store(self,driver):
        
    def lingzuan(self,driver):
        
    def saishi(self,driver):
        
    def talking(self,driver):
    '''
