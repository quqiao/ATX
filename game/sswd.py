#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Game(public.Methods):
    def game_update(self,driver):
        sleep(30)
        if self.images_or_none(driver,'enter_game_01.1920x1080.png'):
            log.info('更新成功')
            return 'ok'
        else:
            log.info('更新失败')
            return None
        
    def game_pre(self,driver):
        self.click_images(driver,"enter_game_01.1920x1080.png")
        if self.wait_gone_images(driver,'enter_game_01.1920x1080.png'):
            log.info('进入游戏前准备成功')
            return 'ok'
        else:
            log.info('进入游戏前准备失败')
            return None
        
    def guide(self,driver):
        '''创建角色'''
        if self.images_or_none(driver,'guide_002.1920x1080.png'):
            self.click_images(driver,"guide_001.1920x1080.png")
            self.click_images(driver,"guide_002.1920x1080.png")
            '''开始游戏'''
            self.click_images(driver,"guide_003.1920x1080.png")
            '''自动战斗'''
            
            for i in range(10000):
                self.click_exists(driver,"guide_004.1920x1080.png")
                self.click_exists(driver,"guide_005.1920x1080.png")
                if self.images_or_none(driver,"guide_006.1920x1080.png",timeout=3):
                    break
            self.click_images(driver,"guide_006.1920x1080.png")
            self.click_images(driver,"guide_007.1920x1080.png")
            self.click_images(driver,"guide_008.1920x1080.png")
            self.click_images(driver,"guide_009.1920x1080.png")
        else:
            print '不用引导'
        if self.wait_gone_images(driver,'guide_006.1920x1080.png'):
            log.info('引导成功')
            return 'ok'
        else:
            log.info('引导失败')
            return None

        
    def game_pay_pre(self,driver):
        self.click_images(driver,"game_pay_pre01.1920x1080.png")
        sleep(2)
        if self.wait_gone_images(driver, 'game_pay_pre01.1920x1080.png'):
            return 'ok'
        else:
            return None 
        
    def game_pay1(self,driver):
        self.click_images(driver,"game_pay01.1920x1080.png")
        sleep(1)
        if self.wait_gone_images(driver, 'game_pay01.1920x1080.png'):
            return 'ok'
        else:
            return None
        
    def basicFunction(self,driver):
        sleep(30)
        self.click_images(driver,"basic_01.1920x1080.png")
        self.click_images(driver,"basic_02.1920x1080.png")
        self.click_images(driver,"basic_03.1920x1080.png")
        self.click_images(driver,"basic_04.1920x1080.png")
        self.click_images(driver,"basic_05.1920x1080.png")
        self.click_images(driver,"basic_06.1920x1080.png")
        self.click_images(driver,"basic_07.1920x1080.png")
        self.click_images(driver,"basic_08.1920x1080.png")
        self.click_images(driver,"basic_09.1920x1080.png")
        #self.click_images(driver,"basic_10.1920x1080.png")
        #self.click_images(driver,"basic_11.1920x1080.png")
        self.click_images(driver,"basic_12.1920x1080.png")
        self.click_images(driver,"basic_13.1920x1080.png")
        sleep(1)
        driver.long_click(1862,613)
        driver.long_click(1200,613)
        self.click_images(driver,"basic_15.1920x1080.png")
        sleep(1)
        driver.long_click(1862,740)
        driver.long_click(1200,613)
        self.click_images(driver,"basic_17.1920x1080.png")
        sleep(1)
        driver.long_click(1862,1016)
        driver.long_click(1200,613)
        if self.wait_gone_images(driver, 'basic_18.1920x1080.png'):
            return 'ok'
        else:
            return None
    
    '''问道商城'''   
    def store(self,driver):
        self.click_images(driver,"store_01.1920x1080.png")
        self.click_images(driver,"store_02.1920x1080.png")
        self.click_images(driver,"store_03.1920x1080.png")
        self.click_images(driver,"store_04.1920x1080.png")
        self.click_images(driver,"store_05.1920x1080.png")
        sleep(1)
        driver.long_click(1800,40) 
        driver.long_click(1200,30) 
        if self.wait_gone_images(driver, 'store_06.1920x1080.png'):
            return 'ok'
        else:
            return None
        
    '''问道首充'''    
    def live(self,driver):
        self.click_images(driver,"live_01.1920x1080.png")
        self.click_images(driver,"live_02.1920x1080.png")
        if self.wait_gone_images(driver, 'live_02.1920x1080.png'):
            return 'ok'
        else:
            return None
    
    '''问道特权'''   
    def gonglue(self,driver):
        self.click_images(driver,"gonglue_01.1920x1080.png")
        self.click_images(driver,"gonglue_02.1920x1080.png")
        if self.wait_gone_images(driver, 'gonglue_02.1920x1080.png'):
            return 'ok'
        else:
            return None
    
    '''问道离线挂机'''    
    def saishi(self,driver):
        self.click_images(driver,"saishi_01.1920x1080.png")
        self.click_images(driver,"saishi_02.1920x1080.png")
        if self.wait_gone_images(driver, 'saishi_02.1920x1080.png'):
            return 'ok'
        else:
            return None
    
    '''问道BOSS大厅'''   
    def lingzuan(self,driver):
        self.click_images(driver,"lingzuan_01.1920x1080.png")
        self.click_images(driver,"lingzuan_02.1920x1080.png")
        self.click_images(driver,"lingzuan_03.1920x1080.png")
        self.click_images(driver,"lingzuan_04.1920x1080.png")
        if self.wait_gone_images(driver, 'lingzuan_04.1920x1080.png'):
            return 'ok'
        else:
            return None
    
    def talking(self,driver):
        self.click_images(driver,"talking_01.1920x1080.png")
        self.click_images(driver,"talking_02.1920x1080.png")
        sleep(1)
        driver(className='android.widget.EditText',index=0).click()
        driver.type(u"毛泽东法轮功江泽民") 
        driver(className='android.widget.Button',index=1).click()
        self.click_images(driver,"talking_03.1920x1080.png")
        self.click_images(driver,"talking_04.1920x1080.png")

        if self.wait_gone_images(driver, 'talking_04.1920x1080.png'):
            return 'ok'
        else:
            return None
        
    def setting(self,driver):
        self.click_images(driver,"setting_01.1920x1080.png")
        self.click_images(driver,"setting_02.1920x1080.png")
        if self.wait_gone_images(driver, 'setting_02.1920x1080.png'):
            log.info('游戏中退出按钮')
            return 'ok'
        else:
            return None
        
    
    def exitgame(self,driver):
        self.click_images(driver,"exitgame_01.1920x1080.png")
        self.click_images(driver,"exitgame_02.1920x1080.png")
        if self.wait_gone_images(driver, 'exitgame_02.1920x1080.png'):
            log.info('游戏中退出按钮')
            return 'ok'
        else:
            return None
        
        
    
