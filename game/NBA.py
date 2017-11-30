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
        driver.swipe(500,439,800,439,50)  # 滑动调整年龄
        self.click_images(driver,"game_update_03.1920x1080.png")
        self.click_images(driver,"game_update_04.1920x1080.png")
        if self.wait_gone_images(driver,'game_update_04.1920x1080.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
        
    def game_pre(self,driver):
        self.click_images(driver,"game_pre_01.1920x1080.png")  # 继续
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

            #self.click_images(driver,"guide_001.1920x1080.png")
            driver.click(963,885)  # 开始
            sleep(2)
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
            sleep(5)
            driver.click(1298,975)  # 继续
            # self.click_images(driver,"guide_003.1920x1080.png")
            '''组建球队'''
            # self.click_images(driver,"guide_004.1920x1080.png")
            # self.click_images(driver,"guide_005.1920x1080.png")
            sleep(6)
            driver.click(959,878)  # 继续
            sleep(2)
            driver.click(900,420)  # 队名输入框
            sleep(1)
            driver.type('wedfg')
            sleep(1)
            driver.click(500,500)
            sleep(1)
            driver.click(950,850)  # 继续
            sleep(5)
            driver.click(1280,468)  # 火箭队
            sleep(1)
            driver.click(960,990)  # 选择并继续
            # self.click_images(driver,"guide_003.1920x1080.png")
            # self.click_images(driver,"guide_006.1920x1080.png")
            # self.click_images(driver,"guide_007.1920x1080.png")
            '''商店'''
            sleep(5)
            driver.swipe(1796,38,1796,38,30)  # 商店
            sleep(6)
            driver.click(280,680)  # 领取
            sleep(6)
            driver.click(1680,1025)  # 打开卡包
            sleep(8)
            driver.click(1680,1025)  # 全部显示
            # self.click_images(driver,"guide_008.1920x1080.png")
            # self.click_images(driver,"guide_009.1920x1080.png")
            # self.click_images(driver,"guide_010.1920x1080.png")
            # self.click_images(driver,"guide_011.1920x1080.png")
            '''升级球队'''
            sleep(3)
            driver.click(1190,1020)  # 升级球队
            sleep(5)
            driver.click(1680,1025)  # 继续
            sleep(3)
            driver.click(890,430)  # 我的球队
            sleep(3)
            driver.click(630,460)  # 可升级球员
            sleep(3)
            driver.click(1289,126)  # 训练球员
            sleep(2)
            driver.click(810,480)  # 升级球员
            sleep(2)
            driver.click(122,955)  # 训练点数
            sleep(1)
            driver.click(1135,720)  # 应用训练
            sleep(2)
            driver.click(665,889)  # 升级
            sleep(5)
            driver.click(980,800)  # 点击继续
            # self.click_images(driver,"guide_012.1920x1080.png")
            # self.click_images(driver,"guide_013.1920x1080.png")
            # self.click_images(driver,"guide_014.1920x1080.png")
            # sleep(3)
            # driver.click(629,450)#可升级球员
            # self.click_images(driver,"guide_015.1920x1080.png")
            # self.click_images(driver,"guide_016.1920x1080.png")
            # self.click_images(driver,"guide_017.1920x1080.png")
            # self.click_images(driver,"guide_018.1920x1080.png")
            # self.click_images(driver,"guide_019.1920x1080.png")
            # sleep(5)
            # driver.click(500,500)
            '''在线赛事'''
            sleep(3)
            driver.click(855,898)  # 在线赛事
            sleep(2)
            driver.click(960,680)  # 好的
            for i in range(4):
                sleep(2)
                driver.click(970,980)  # 领取并完成
            sleep(5)
            driver.click(1680,1025)  # 打开卡包
            sleep(5)
            driver.click(1680,1025)  # 全部显示
            sleep(1)
            driver.click(1680,1025)  # 继续
            log.info('游戏引导完成')
            # self.click_images(driver,"guide_020.1920x1080.png")
        else:
            driver.click(1320,980)  # 在线赛事
            sleep(2)
            driver.click(960,660)  # 好的
            log.info('游戏已过引导')
        if self.wait_gone_images(driver,'guide_020.1920x1080.png'):
            log.info('引导成功')
            return 'ok'
        else:
            log.info('引导失败')
            return None

    def basicFunction(self,driver):
        sleep(1)
        driver.click(15,585)  # 打开菜单
        sleep(2)
        driver.click(120,730)  # 我的球队
        sleep(2)
        driver.click(15,585)  # 打开菜单
        sleep(2)
        driver.click(120,840)  # 我的球队
        sleep(2)
        driver.click(15,585)  # 打开菜单
        sleep(2)
        driver.click(120,185)  # 在线赛事
        sleep(2)
        driver.click(1625,45)  # 篮球
        sleep(2)
        driver.click(40,40)  # 返回
        sleep(2)
        driver.click(1700,60)  # 邮件
        sleep(2)
        driver.click(1570,86)  # 关闭
        sleep(2)
        driver.click(1790,45)  # 购物车
        sleep(2)
        driver.click(40,40)  # 返回
        sleep(2)
        if self.wait_gone_images(driver,'guide_001.1920x1080.png'):
            log.info('基本功能检查成功')
            return 'ok'
        else:
            log.info('基本功能检查失败')
            return None

    def live(self,driver):
        log.info('NBA暂时没有直播')
        if self.wait_gone_images(driver,'guide_001.1920x1080.png'):
            log.info('直播忽略成功')
            return 'ok'
        else:
            log.info('直播忽略失败')
            return None

    def gonglue(self,driver):
        log.info('NBA暂时没有攻略')
        if self.wait_gone_images(driver,'guide_001.1920x1080.png'):
            log.info('攻略忽略成功')
            return 'ok'
        else:
            log.info('攻略忽略失败')
            return None

    def saishi(self,driver):
        log.info('NBA暂时没有赛事')
        if self.wait_gone_images(driver,'guide_001.1920x1080.png'):
            log.info('赛事忽略成功')
            return 'ok'
        else:
            log.info('赛事忽略失败')
            return None

    def lingzuan(self,driver):
        log.info('NBA暂时没有领钻')
        if self.wait_gone_images(driver,'guide_001.1920x1080.png'):
            log.info('领钻忽略成功')
            return 'ok'
        else:
            log.info('领钻忽略失败')
            return None

    def store(self,driver):
        log.info('NBA暂时没有市场')
        if self.wait_gone_images(driver,'guide_001.1920x1080.png'):
            log.info('市场忽略成功')
            return 'ok'
        else:
            log.info('市场忽略失败')
            return None

    def talking(self,driver):
        log.info('NBA暂时没有对话')
        if self.wait_gone_images(driver,'guide_001.1920x1080.png'):
            log.info('对话忽略成功')
            return 'ok'
        else:
            log.info('对话忽略失败')
            return None
