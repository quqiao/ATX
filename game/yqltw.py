#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep,time
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Game(public.Methods):
    def game_update(self,driver):
        for i in range(8):
            sleep(30)
            driver.click(500,500)
        if self.wait_gone_images(driver,'game_pre_01.1920x1080.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
        
    def game_pre(self,driver):
        self.click_images(driver,"game_pre_01.1920x1080.png")
        self.click_images(driver,"game_pre_02.1920x1080.png")
        self.click_images(driver,"game_pre_03.1920x1080.png")
        if self.wait_gone_images(driver,'game_pre_03.1920x1080.png'):
            log.info('进入游戏前准备成功')
            return 'ok'
        else:
            log.info('进入游戏前准备失败')
            return None
        
    def guide(self,driver):
        '''开始引导'''
        if self.images_or_none(driver,"guide_001.1920x1080.png"):
            driver.click(780,930)
            driver(className='android.widget.EditText',index=0).click()
            driver.type('12')
            sleep(1)
            driver.click(1836,930)
            self.click_images(driver,"guide_002.1920x1080.png")
            self.click_images(driver,"guide_003.1920x1080.png")
            self.click_images(driver,"guide_004.1920x1080.png")
            sleep(5)
            driver.click(500,500)
            sleep(1)
            driver.click(500,500)
            sleep(10)
            self.images_or_none(driver,"guide_005.1920x1080.png")
            sleep(1)
            driver.click(1410,320)
            sleep(1)
            driver.click(928,720)
            sleep(1)
            driver.click(928,720)
            sleep(1)
            driver.click(0.5,0.5)
            '''舞创商城'''
            self.images_or_none(driver,"guide_006.1920x1080.png")
            sleep(1)
            driver.click(950,620)
            self.images_or_none(driver,"guide_007.1920x1080.png")
            sleep(1)
            driver.click(920,570)
            self.images_or_none(driver,"guide_008.1920x1080.png")
            sleep(1)
            driver.click(900,316)
            driver.click(900,316)
            driver.click(900,316)
            driver.click(1823,50)   #返回
            self.images_or_none(driver,"guide_007.1920x1080.png")#返回
            driver.click(1823,50)   #返回
            '''活跃'''
            self.images_or_none(driver,"guide_006.1920x1080.png")
            sleep(1)
            driver.click(1735,40)   #活跃
            sleep(2)
            driver.click(856,150)   #常规任务
            sleep(2)
            driver.click(1288,900) #领取奖励
            sleep(2)
            driver.click(1288,900) #接受任务
            sleep(2)
            driver.click(1668,90) #关闭
            '''游戏大厅'''
            self.images_or_none(driver,"guide_006.1920x1080.png")
            sleep(2)
            driver.click(930,399) #游戏大厅
            self.images_or_none(driver,"guide_009.1920x1080.png")
            sleep(2)
            driver.click(65,364) #设置
            sleep(2)
            driver.click(330,265) #背包
            sleep(2)
            driver.click(1827,200) #配饰
            sleep(2)
            driver.click(1248,286) #头像
            sleep(2)
            driver.click(1823,50)   #返回
            '''活跃'''
            sleep(2)
            driver.click(1352,43)   #返回
            sleep(2)
            driver.click(856,150)   #常规任务
            sleep(2)
            driver.click(1288,900) #领取奖励
            sleep(2)
            driver.click(1288,900) #接受任务
            sleep(2)
            driver.click(1668,90) #关闭
            sleep(2)
            driver.click(500,500)
            sleep(2)
            driver.click(500,500)
            '''创建房间'''
            sleep(2)
            driver.click(1027,983) #创建房间
            sleep(2)
            driver.click(1150,850) #确定
            self.images_or_none(driver,"guide_010.1920x1080.png")
            sleep(2)
            driver.click(1560,980) #随机场景
            sleep(2)
            driver.click(1150,310) #随机歌曲
            sleep(2)
            driver.click(939,985) #确定
            sleep(2)
            driver.click(1800,964) #开始
            '''第一次跳舞'''
            self.images_or_none(driver,"guide_011.1920x1080.png")
            driver.click(1710,860) #下
            driver.click(1530,730) #左
            driver.click(1710,530) #上
            sleep(2)
            driver.click(190,766) #beat
            sleep(2)
            driver.click(190,766) #beat
            sleep(2)
            driver.click(1710,860) #下
            driver.click(1530,730) #左
            driver.click(1710,530) #上
            sleep(10)
            driver.click(190,766) #beat
            sleep(2)
            driver.click(190,766) #beat
            sleep(3)
            driver.click(500,500)
            sleep(3)
            driver.click(1710,860) #下
            driver.click(1530,730) #左
            driver.click(1710,530) #上
            sleep(10)
            driver.click(190,766) #beat
            sleep(2)
            '''大厅'''
            self.images_or_none(driver,"guide_010.1920x1080.png")
            driver.click(1818,50) #大厅
            self.images_or_none(driver,"guide_009.1920x1080.png")
            driver.click(1866,50) #社区
            self.images_or_none(driver,"guide_006.1920x1080.png")
            driver.click(1735,36) #活跃
            sleep(2)
            driver.click(856,150)   #常规任务
            sleep(2)
            driver.click(1288,900) #领取奖励
            sleep(2)
            driver.click(1288,900) #接受任务
            sleep(2)
            driver.click(1668,90) #关闭
            '''魔法屋'''
            self.images_or_none(driver,"guide_006.1920x1080.png")
            driver.click(1620,55) #魔法屋
            sleep(2)
            driver.click(969,600) #碎片工坊
            sleep(2)
            driver.click(0.5,0.5)
            sleep(2)
            driver.click(0.5,0.5)
            sleep(2)
            driver.click(789,750) #合成
            sleep(2)
            driver.click(1168,731) #确定  
            sleep(2)
            driver.click(0.5,0.5)
            sleep(2)
            driver.click(0.5,0.5)
            sleep(2)
            driver.click(1710,145) #关闭
            sleep(2)
            driver.click(0.5,0.5)
            '''活跃'''
            sleep(2)
            driver.click(1735,36) #活跃
            sleep(2)
            driver.click(856,150)   #常规任务
            sleep(2)
            driver.click(1288,900) #领取奖励
            sleep(2)
            driver.click(1288,900) #接受任务
            sleep(2)
            driver.click(1668,90) #关闭
        else:
            print '引导已完成'
        
        if self.wait_gone_images(driver,'guide_010.1920x1080.png'):
            log.info('游戏引导结束')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
        
        """
        '''扭蛋'''
        self.click_images(driver,"guide_041.1920x1080.png")
        sleep(2)
        driver.click(0.5,0.5)
        self.click_images(driver,"guide_042.1920x1080.png")
        self.click_images(driver,"guide_043.1920x1080.png")
        sleep(2)
        driver.click(0.5,0.5)
        self.click_images(driver,"guide_044.1920x1080.png")
        '''活跃'''
        self.click_images(driver,"guide_022.1920x1080.png")
        self.click_images(driver,"guide_023.1920x1080.png")
        self.click_images(driver,"guide_013.1920x1080.png")
        self.click_images(driver,"guide_014.1920x1080.png")
        self.click_images(driver,"guide_015.1920x1080.png")
        '''徽章馆'''
        self.click_images(driver,"guide_045.1920x1080.png")
        sleep(2)
        driver.click(0.5,0.5)
        self.click_images(driver,"guide_046.1920x1080.png")
        self.click_images(driver,"guide_047.1920x1080.png")
        self.click_images(driver,"guide_048.1920x1080.png")
        self.click_images(driver,"guide_049.1920x1080.png")
        self.click_images(driver,"guide_050.1920x1080.png")
        sleep(2)
        driver.click(0.5,0.5)
        self.click_images(driver,"guide_051.1920x1080.png")
        '''活跃'''
        self.click_images(driver,"guide_022.1920x1080.png")
        self.click_images(driver,"guide_023.1920x1080.png")
        self.click_images(driver,"guide_013.1920x1080.png")
        self.click_images(driver,"guide_014.1920x1080.png")
        self.click_images(driver,"guide_015.1920x1080.png")
        sleep(2)
        driver.click(0.5,0.5)
        '''时空裂痕'''
        self.click_images(driver,"guide_052.1920x1080.png")
        self.click_images(driver,"guide_053.1920x1080.png")
        self.click_images(driver,"guide_054.1920x1080.png")
        '''第二次跳舞'''
        for i in range(100):
            self.click_images(driver,"guide_055.1920x1080.png")
            if self.exist(driver,"guide_056.1920x1080.png"):
                break
        driver.click(0.5,0.5)
        '''第三次跳舞'''
        """
        
        
