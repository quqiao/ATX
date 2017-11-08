#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Game(public.Methods):
    def game_update(self,driver):
        sleep(15)
        self.click_images(driver,"game_update_01.1920x1080.png")
        if self.wait_gone_images(driver,'game_update_01.1920x1080.png'):
            log.info('更新成功')
            return 'ok'
        else:
            log.info('更新失败')
            return None
               
    def game_pre(self,driver):
        self.click_images(driver,"game_pre_01.1920x1080.png")
        if self.wait_gone_images(driver,'game_pre_01.1920x1080.png'):
            log.info('更新成功')
            return 'ok'
        else:
            log.info('更新失败')
            return None
        
    def guide(self,driver):
        '''开始引导'''
        if self.images_or_none(driver,'guide_001.1920x1080.png'):
            #self.images_or_none(driver,'guide_001.1920x1080.png')#对话
            sleep(2)
            driver.click(1820,930)#故事剧情
            '''关卡1'''
            sleep(3)
            driver.click(250,355)#关卡1
            sleep(2)
            for i in range(6):
                sleep(1)
                driver.click(500,500)
            sleep(2)
            driver.click(1479,376)#去战斗
            sleep(2)
            self.images_or_none(driver,'guide_002.1920x1080.png')#全部
            sleep(1)
            driver.swipe(593,969,455,550,50)#滑动位置
            sleep(1)
            driver.click(1723,966)#进入战斗
            sleep(3)
            driver.click(1638,994)#跳过对话
            sleep(3)
            self.images_or_none(driver,'guide_003.1920x1080.png')#升级啦
            sleep(1)
            driver.click(955,533)#确定
            sleep(1)
            driver.click(1687,941)#继续
            '''关卡2'''
            sleep(2)
            driver.click(466,595)#关卡2
            sleep(2)
            driver.click(1479,376)#去战斗
            self.images_or_none(driver,'guide_002.1920x1080.png')#全部
            sleep(1)
            driver.swipe(425,450,680,520,50)#滑动位置
            sleep(2)
            driver.click(1723,966)#进入战斗
            sleep(3)
            driver.click(1638,994)#跳过对话
            sleep(3)
            self.images_or_none(driver,'guide_004.1920x1080.png')#胜利
            sleep(2)
            driver.click(1687,941)#继续
            sleep(2)
            driver.click(955,687)#确定#
            '''新任务'''
            sleep(2)
            driver.click(1440,520)#新任务
            sleep(2)
            driver.click(716,450)#领取奖励
            sleep(3)
            driver.click(955,687)#确定
            sleep(1)
            driver.click(1290,526)#点击空白处
            sleep(1)
            driver.click(1366,775)#宝箱
            sleep(1)
            driver.click(1366,775)#宝箱
            sleep(1)
            for i in range(6):
                driver.click(960,530)#兑换道具
                sleep(1)
            sleep(5)
            driver.click(958,941)#确定获得道具
            sleep(6)
            driver.click(955,1010)#点击继续
            sleep(2)
            driver.click(955,687)#确定
            sleep(2)
            driver.click(1820,930)#故事剧情
            sleep(2)
            driver.click(1820,930)#故事剧情
            '''关卡3'''
            sleep(2)
            driver.click(794,700)#关卡3
            sleep(1)
            for i in range(9):
                sleep(1)
                driver.click(500,500)
            sleep(2)
            driver.click(1479,376)#去战斗
            self.images_or_none(driver,'guide_002.1920x1080.png')#全部
            sleep(1)
            driver.swipe(750,970,680,750,50)#滑动位置
            sleep(2)
            driver.click(1723,966)#进入战斗
            sleep(3)
            driver.click(1638,994)#跳过对话
            sleep(20)
            self.images_or_none(driver,'guide_003.1920x1080.png')#升级啦
            sleep(2)
            driver.click(955,533)#确定
            sleep(2)
            driver.click(1687,941)#继续
            '''关卡4'''
            sleep(2)
            driver.click(1230,660)#关卡4
            sleep(2)
            driver.click(1479,376)#去战斗
            self.images_or_none(driver,'guide_002.1920x1080.png')#全部
            sleep(1)
            driver.swipe(628,662,450,530,50)#滑动位置
            sleep(2)
            driver.click(1723,966)#进入战斗
            sleep(3)
            driver.click(1638,994)#跳过对话
            sleep(20)
            self.images_or_none(driver,'guide_004.1920x1080.png')#胜利
            sleep(1)
            driver.click(1687,941)#继续
            sleep(2)
            driver.click(480,980)#章节奖励1
            sleep(2)
            driver.click(955,710)#领取
            '''关卡5'''
            sleep(2)
            driver.click(890,420)#关卡5
            sleep(2)
            driver.click(1479,376)#去战斗
            self.images_or_none(driver,'guide_002.1920x1080.png')#全部
            sleep(1)
            driver.click(1723,966)#进入战斗
            sleep(3)
            driver.click(1638,994)#跳过对话
            sleep(15)
            self.images_or_none(driver,'guide_004.1920x1080.png')#胜利
            sleep(1)
            driver.click(1687,941)#继续
            sleep(2)
            driver.click(790,966)#章节奖励2
            sleep(2)
            driver.click(955,710)#领取
            '''关卡6'''
            sleep(2)
            driver.click(1472,283)#关卡6
            sleep(2)
            for i in range(11): 
                sleep(1)
                driver.click(500,500)
            sleep(2)
            driver.click(1479,376)#去战斗
            self.images_or_none(driver,'guide_002.1920x1080.png')#全部
            sleep(1)
            driver.click(1723,966)#进入战斗
            sleep(3)
            driver.click(1638,994)#跳过对话
            sleep(20)
            self.images_or_none(driver,'guide_003.1920x1080.png')#升级啦
            sleep(2)
            driver.click(955,533)#确定
            sleep(3)
            driver.click(1687,941)#继续
            sleep(3)
            driver.click(955,687)#确定
            '''新任务'''
            sleep(2)
            driver.click(1440,520)#新任务
            sleep(1)
            driver.click(716,450)#领取奖励
            sleep(6)
            driver.click(955,687)#确定
            sleep(1)
            driver.click(1290,526)#点击空白处
            sleep(1)
            driver.click(1366,775)#宝箱
            sleep(1)
            driver.click(1366,775)#宝箱
            sleep(1)
            for i in range(5):
                driver.click(960,530)#兑换道具
                sleep(1)
            sleep(3)
            driver.click(958,941)#确定获得道具
            sleep(6)
            driver.click(955,1010)#点击继续
            sleep(2)
            driver.click(955,687)#确定
            '''武将'''
            sleep(2)
            driver.click(80,992)#武器
            sleep(3)
            driver.click(575,486)#美美
            '''升级'''
            sleep(3)
            driver.click(1390,170)#升级
            sleep(3)
            driver.click(1570,960)#一键升级
            sleep(2)
            driver.click(125,45)#详情
            sleep(2)
            driver.click(125,45)#武将管理
            sleep(2)
            driver.click(1820,930)#故事剧情
            sleep(2)
            driver.click(1820,930)#故事剧情
            '''关卡7'''
            sleep(2)
            driver.click(300,490)#关卡7
            for i in range(7):
                sleep(1)
                driver.click(500,500)
            sleep(1)
            driver.click(1479,376)#去战斗
            self.images_or_none(driver,'guide_002.1920x1080.png')#全部
            sleep(1)
            driver.swipe(750,970,720,355,50)#滑动位置
            sleep(1)
            driver.click(1723,966)#进入战斗
            sleep(3)
            driver.click(1638,994)#跳过对话
            sleep(20)
            self.images_or_none(driver,'guide_004.1920x1080.png')#胜利
            sleep(1)
            driver.click(1687,941)#继续
            '''关卡8'''
            sleep(2)
            driver.click(710,280)#关卡8
            sleep(2)
            driver.click(1479,376)#去战斗
            self.images_or_none(driver,'guide_002.1920x1080.png')#全部
            sleep(1)
            driver.swipe(710,270,500,350,50)#滑动位置
            sleep(1)
            driver.click(1723,966)#进入战斗
            sleep(3)
            driver.click(1638,994)#跳过对话
            sleep(10)
            self.images_or_none(driver,'guide_004.1920x1080.png')#胜利
            sleep(1)
            driver.click(1687,941)#继续
            '''关卡9'''
            sleep(2)
            driver.click(670,680)#关卡9
            for i in range(8):
                sleep(1)
                driver.click(500,500)
            sleep(1)
            driver.click(1479,376)#去战斗
            self.images_or_none(driver,'guide_002.1920x1080.png')#全部
            sleep(1)
            driver.swipe(460,270,723,350,50)#滑动位置
            sleep(1)
            driver.click(1723,966)#进入战斗
            sleep(3)
            driver.click(1638,994)#跳过对话
            sleep(36)
            for i in range(4):
                sleep(1)
                driver.click(500,500)
            sleep(6)
            driver.click(955,369)#解锁宝箱
            '''宝箱'''
            sleep(2)
            driver.click(220,990)#宝箱
            sleep(2)
            driver.click(420,330)#白银宝箱
            sleep(2)
            driver.click(965,816)#购买
            for i in range(11):
                sleep(1)
                driver.click(965,535)
            sleep(6)
            driver.click(958,941)#确定获得道具
            sleep(6)
            driver.click(955,1010)#点击继续
            sleep(2)
            driver.click(955,687)#确定
            sleep(2)
            driver.click(125,45)#返回
            '''武将'''
            sleep(2)
            driver.click(80,992)#武器
            sleep(2)
            driver.click(1338,484)#刘备
            '''升级'''
            sleep(2)
            driver.click(1390,170)#升级
            sleep(2)
            driver.click(1570,960)#一键升级
            sleep(2)
            '''进阶'''
            driver.click(1210,170)#进阶
            sleep(2)
            driver.click(1419,969)#统领
            sleep(2)
            driver.click(1520,750)#无兵种
            sleep(2)
            driver.click(1520,630)#扫荡
            sleep(2)
            driver.click(1000,380)#扫1次
            sleep(6)
            driver.click(950,530)#确定
            sleep(2)
            driver.click(1230,900)#确定2
            sleep(2)
            driver.click(1629,122)#关闭
            sleep(2)
            driver.click(536,883)#统领2
            sleep(2)
            driver.click(1420,962)#进阶2
            sleep(5)
            driver.click(950,900)#确定2
            sleep(2)
            driver.click(125,45)#详情
            sleep(2)
            driver.click(125,45)#武将管理
            sleep(1)
            driver.click(1820,930)#故事剧情
            sleep(1)
            driver.click(1820,930)#故事剧情
            '''关卡10'''
            sleep(2)
            driver.click(1085,680)#关卡10
            sleep(1)
            driver.click(1479,376)#去战斗
            self.images_or_none(driver,'guide_002.1920x1080.png')#全部
            sleep(1)
            driver.swipe(600,970,395,750,50)#滑动位置
            sleep(1)
            driver.click(1723,966)#进入战斗
            sleep(3)
            driver.click(1638,994)#跳过对话
            sleep(32)
            driver.click(1687,941)#继续
            sleep(3)
            driver.click(480,980)#章节奖励1
            sleep(2)
            driver.click(955,710)#领取
            '''关卡11'''
            sleep(2)
            driver.click(1025,260)#关卡11
            sleep(1)
            driver.click(1479,376)#去战斗
            sleep(6)
            driver.click(1723,966)#进入战斗
            sleep(3)
            driver.click(1638,994)#跳过对话
            sleep(30)
            driver.click(1687,941)#继续
            '''关卡12'''
            sleep(2)
            driver.click(1480,355)#关卡12
            sleep(1)
            driver.click(1479,376)#去战斗
            sleep(12)
            driver.click(1723,966)#进入战斗
            sleep(5)
            driver.click(1638,994)#跳过对话
            sleep(25)
            self.images_or_none(driver,'guide_002.1920x1080.png')#失败
            sleep(1)
            driver.click(1691,669)#再战
            sleep(3)
            driver.swipe(390,450,490,355,50)#滑动位置
            sleep(2)
            driver.click(1723,966)#进入战斗
            sleep(33)
            for i in range(7):
                sleep(1)
                driver.click(965,535)
            sleep(5)
            driver.click(1687,941)#继续
            sleep(3)
            driver.click(958,695)#任务完成确定
            sleep(2)
            driver.click(1440,520)#新任务
            sleep(1)
            driver.click(716,450)#领取奖励
            sleep(5)
            driver.click(950,700)#确定
            sleep(1)
            driver.click(1290,526)#点击空白处
            sleep(1)
            driver.click(1366,775)#宝箱
            sleep(1)
            driver.click(1366,775)#宝箱
            for i in range(5):
                sleep(1)
                driver.click(965,535)
            sleep(3)
            driver.click(958,941)#确定获得道具
            sleep(3)
            driver.click(958,703)#确定获得道具
            sleep(2)
            driver.click(1820,930)#故事剧情
            sleep(2)
            driver.click(125,45)#返回
        else:
            print "引导已完成"
        if self.wait_gone_images(driver,'guide_001.1920x1080.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None

    def basicFunction(self,driver):
        sleep(2)
        driver.click(1352,150)#成长基金
        sleep(2)
        driver.click(50,39)#返回
        sleep(2)
        driver.click(1472,150)#签到
        sleep(2)
        driver.click(50,39)#返回
        sleep(2)
        driver.click(1600,150)#首充
        sleep(2)
        driver.click(50,39)#返回
        sleep(2)
        driver.click(1740,150)#充值
        sleep(2)
        driver.click(50,39)#返回
        sleep(2)
        driver.click(1860,150)#活动
        sleep(3)
        driver.click(50,39)#返回
        sleep(3)
        driver.click(1239,46)#体力
        sleep(2)
        driver.click(1555,580)#点击空白处
        sleep(2)
        driver.click(1550,46)#银币
        sleep(2)
        driver.click(1555,580)#点击空白处
        sleep(2)
        driver.click(1850,46)#金币
        sleep(2)
        driver.click(50,39)#返回
        sleep(2)
        driver.click(60,220)#邮件
        sleep(2)
        driver.click(1518,106)#关闭
        sleep(2)
        driver.click(60,350)#限时礼包
        sleep(2)
        driver.click(50,39)#返回
        sleep(2)
        driver.click(60,460)#登录福利
        sleep(2)
        driver.click(1480,450)#福利关闭
        sleep(2)
        driver.click(90,990)#武将
        sleep(2)
        driver.click(50,39)#返回
        sleep(2)
        driver.click(220,1000)#宝箱
        sleep(2)
        driver.click(50,39)#返回
        sleep(2)
        driver.click(350,1000)#背包
        sleep(2)
        driver.click(50,39)#返回
        sleep(2)
        if self.images_or_none(driver, 'basicFunction_01.1920x1080.png'):
            return 'ok'
        else:
            return None

    def store(self,driver):
        if self.wait_gone_images(driver, 'exitgame_01.1920x1080.png'):
            log.info('游戏中确定退出')
            return 'ok'
        else:
            return None
        print "暂时没有"

    def live(self,driver):
        if self.wait_gone_images(driver, 'exitgame_01.1920x1080.png'):
            log.info('游戏中确定退出')
            return 'ok'
        else:
            return None
        print "暂时没有"


    def gonglue(self,driver):
        if self.wait_gone_images(driver, 'exitgame_01.1920x1080.png'):
            log.info('游戏中确定退出')
            return 'ok'
        else:
            return None
        print "暂时没有"
         
    def saishi(self,driver):
        if self.wait_gone_images(driver, 'exitgame_01.1920x1080.png'):
            log.info('游戏中确定退出')
            return 'ok'
        else:
            return None
        print "暂时没有"
        
    def lingzuan(self,driver):
        if self.wait_gone_images(driver, 'exitgame_01.1920x1080.png'):
            log.info('游戏中确定退出')
            return 'ok'
        else:
            return None
        print "暂时没有"
        
    def talking(self,driver):
        sleep(2)
        driver.click(60,600)#谈话
        sleep(2)
        driver.click(300,1000)#输入框
        sleep(1)
        driver(className='android.widget.EditText',index=0).click()
        driver.type(u"毛泽东法轮功江泽民")
        sleep(2)
        driver(className='android.widget.Button',index=1).click()
        sleep(2)
        driver.click(800,1020)#发送按钮
        sleep(2)
        driver.click(930,530)#关闭对话框
        sleep(2)
        if self.images_or_none(driver, 'talking_01.1920x1080.png'):
            log.info('游戏中退出按钮')
            return 'ok'
        else:
            return None

    def setting(self,driver):
        sleep(2)
        driver.click(200,90)#头像
        sleep(2)
        driver.click(900,339)#系统设置
        sleep(2)
        driver.click(960,760)#退出游戏
        if self.wait_gone_images(driver, 'setting_01.1920x1080.png'):
            log.info('游戏中退出按钮')
            return 'ok'
        else:
            return None
  
    def exitgame(self,driver):
        sleep(2)
        driver.click(1200,720)#确定退出游戏
        if self.wait_gone_images(driver, 'exitgame_01.1920x1080.png'):
            log.info('游戏中确定退出')
            return 'ok'
        else:
            return None