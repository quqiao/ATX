#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import public.methods as public
import configure
from public import logutils
log = logutils.getLogger(__name__)


class Game(public.Methods):
    
    def game_update(self,driver):
        driver.prepare_ime()
        sleep(30)
        self.click_images(driver,"exit.1920x1080.png")
        driver.start_app(configure.package_name,configure.activity_name)
        self.click_images(driver,"ares.1920x1080.png")
        self.click_images(driver,"enter_game1.1920x1080.png")
        if self.wait_gone_images(driver, 'enter_game1.1920x1080.png'):
            return 'ok'
        else:
            return None
            

    def enter_game(self, driver):
        '''进入游戏，有引导过引导'''
        #sleep(20)
        #driver.prepare_ime()
        self.click_images(driver,"ares.1920x1080.png")
        self.click_images(driver,"enter_game1.1920x1080.png")
        if self.wait_gone_images(driver, 'enter_game1.1920x1080.png'):
            return 'ok'   
        else:
            return None
        """
        if self.guide_exist(driver,'guide_001'):  #判断是否需要过指引
            result = self.game_click(driver, 'guide')  #过指引
            return result
        else:
            result = self.game_click2(driver, 'enter_game')      #不需要过指引的操作
            return result
        """
    
    def game_pre(self,driver):
        log.info('枪战没有游戏前准备')
        if self.wait_gone_images(driver, 'exists_01.1920x1080.png'):
            return 'ok'
        else:
            return None 

       
    def guide(self,driver):
        '''引导第一次战斗'''
        if self.images_or_none(driver,'guide_001.1920x1080.png'):
            sleep(1)
            driver.click(1360,800)  # 随机
            sleep(2)
            driver.click(965,956)  # 进入游戏
            sleep(2)
            self.images_or_none(driver,'guide_002.1920x1080.png')
            sleep(1)
            driver.click(900,750)  # 跳过
            sleep(2)
            driver.click(900,500)  # 关闭弹出框
            sleep(2)
            driver.click(780,1024)  # 战斗
            sleep(2)
            driver.click(400,590)  # 单人模式
            sleep(2)
            driver.click(610,480)  # 机器人关卡
            sleep(2)
            driver.click(398,500)  # 第一个机器人关卡
            sleep(2)
            driver.click(1385,850)  # 开始
            sleep(2)
            self.images_or_none(driver,'guide_029.1920x1080.png')
            sleep(1)
            driver.click(380,930)  # 确定
            sleep(2)
            driver.click(50,39)  # 设置
            sleep(2)
            driver.click(1366,863)  # 退出战斗
            sleep(2)
            driver.click(810,650)  # 确定退出战斗


            '''商城'''
            self.images_or_none(driver,'guide_004.1920x1080.png')
            sleep(1)
            driver.long_click(1819,989)  # 点击商城
            # driver.long_click(1209,658)
            sleep(2)
            driver.click(900,500)  # 关闭弹出框
            sleep(2)
            driver.click(669,1024)  # 超级装备
            sleep(2)
            driver.click(1160,738)  # 购买一次
            sleep(6)
            driver.click(900,500)  # 任意键
            sleep(2)
            driver.click(1180,925)  # 确定
            sleep(2)
            driver.click(1180,925)  # 关闭弹出框
            '''装备'''
            sleep(2)
            driver.long_click(1869,45)  # 返回
            # driver.long_click(1243,30)
            sleep(2)
            driver.click(1190,418)  # 装备
            sleep(2)
            driver.click(380,400)  # 主武器
            sleep(3)
            driver.click(315,850)  # 装备
            sleep(3)
            '''主页'''
            sleep(2)
            driver.click(520,1010)  # 主页
            sleep(2)
            driver.click(1180,925)  # 关闭弹出框
            '''快速战斗'''
            driver.click(1300,830)  # 快速战斗
            sleep(2)
            driver.click(1500,150)  # 组队
            sleep(2)
            self.images_or_none(driver,'guide_029.1920x1080.png')
            sleep(1)
            driver.click(380,930)  # 确定
            sleep(2)
            driver.click(50,39)  # 设置
            sleep(2)
            driver.click(1366,863)  # 退出战斗
            sleep(2)
            driver.click(810,650)  # 确定退出战斗
            '''关闭广告'''
            sleep(2)
            driver.click(1700,100)  # 关闭广告
            sleep(2)
            driver.click(1700,100)  # 关闭广告
            sleep(2)
            driver.click(730,880)  # 暂不教学
            sleep(2)
            driver.click(1225,280)  # 关闭获得物品
            sleep(2)
            driver.click(1700,100)  # 关闭广告
            sleep(2)
            driver.click(950,695)  # 获得确定
            sleep(2)
            driver.click(1225,280)  # 关闭获得物品
            sleep(2)
        else:
            print "不过引导，关闭广告"
            if self.images_or_none(driver, 'exists_05.1920x1080.png',timeout=10):
                self.click_images(driver,"exists_05.1920x1080.png")
                for i in xrange(100):
                    self.click_exists(driver,"pay_01.1920x1080.png")
                    sleep(1)
                    self.click_exists(driver,"game_pre_01.1920x1080.png")
                    sleep(1)
                    if self.exist(driver,'exists_01.1920x1080.png'):
                        print 'fail'
                        break
                else:
                    for i in xrange(100):
                        self.click_exists(driver,"pay_01.1920x1080.png")
                        sleep(1)
                        self.click_exists(driver,"game_pre_01.1920x1080.png")
                        sleep(1)
                        if self.exist(driver,'exists_01.1920x1080.png'):
                            print 'fail'
                            break
        if self.wait_gone_images(driver,'guide_006.1920x1080.png'):
            log.info('引导成功')
            return 'ok'
        else:
            log.info('引导失败')
            return None    
            
    def game_pay_pre(self, driver):
        self.click_images(driver,"game_pay_pre01.1920x1080.png")
        sleep(2)
        if self.images_or_none(driver, 'exists_03.1920x1080.png'):
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
        '''逐步遍历基本功能'''
        driver.click(200,335)  # 推荐
        sleep(2)
        driver.click(1579,120)  # 关闭
        sleep(2)
        driver.click(200,800)  # 邮件
        sleep(2)
        driver.long_click(1860,36)  # 返回
        sleep(2)
        driver.click(1200,250)  # 角色
        sleep(2)
        driver.long_click(1860,36)  # 返回
        sleep(2)
        driver.click(1200,450)  # 装备
        sleep(2)
        driver.long_click(1860,36)  # 返回
        sleep(2)
        driver.click(1200,650)  # 任务
        sleep(2)
        driver.long_click(1860,36)  # 返回
        sleep(2)
        driver.click(1600,250)  # 机甲
        sleep(2)
        driver.click(720,880)  # 暂不教学
        sleep(2)
        driver.click(1560,450)  # 天赋
        sleep(2)
        driver.click(1560,660)  # 排行
        sleep(2)
        driver.long_click(1860,36)  # 返回
        sleep(2)
        driver.click(789,1020)  # 战斗
        sleep(2)
        driver.click(1060,1015)  # 创造
        sleep(2)
        driver.click(1723,92)  # 返回
        sleep(2)
        driver.click(1300,1020)  # 强化
        sleep(2)
        driver.click(1560,1020)  # 社交
        sleep(2)
        driver.click(530,1020)  # 主页
        sleep(2)
        if self.images_or_none(driver, 'basic_03.1920x1080.png'):
            return 'ok'
        else:
            return None
    
    '''枪战直播'''   
    def live(self,driver):
        driver.click(200,650)  # 直播
        sleep(6)
        driver.click(130,785)  # 直播间
        sleep(2)
        driver.long_click(1860,60)  # 关闭
        sleep(2)
        if self.images_or_none(driver, 'basic_07.1920x1080.png'):
            return 'ok'
        else:
            return None
    
    '''枪战攻略'''   
    def gonglue(self,driver):
        sleep(1)
        driver.click(369,829)  # 攻略
        sleep(6)
        driver.click(90,330)  # 红人
        sleep(2)
        driver.click(90,580)  # 攻略
        sleep(2)
        driver.click(90,820)  # 个人
        sleep(2)
        driver.click(1696,1024)  # 关闭
        if self.images_or_none(driver, 'basic_11.1920x1080.png'):
            return 'ok'
        else:
            return None
        
    
    '''枪战赛事'''    
    def saishi(self,driver):
        sleep(1)
        driver.click(520,829)  # 赛事
        sleep(6)
        driver.click(68,350)  # 英雄榜
        sleep(2)
        driver.click(68,580)  # 小队
        sleep(2)
        driver.click(68,829)  # 我的
        sleep(2)
        driver.click(1696,1024)  # 关闭
        if self.images_or_none(driver, 'basic_13.1920x1080.png'):
            return 'ok'
        else:
            return None
       
    '''枪战领钻'''   
    def lingzuan(self,driver):
        # self.click_images(driver,"basic_15.1920x1080.png")
        # sleep(2)
        # driver(className="android.view.View",description='每日成功分享（0/1）').click()
        # #self.click_images(driver,"choujiang.1920x1080.png")
        # #self.click_images(driver,"lingzuian_04.1920x1080.png")
        # sleep(2)
        # driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=0).click()
        # #sleep(3)
        # #driver(className="android.widget.LinearLayout",resourceId="com.tencent.mm:id/hf").click()
        # self.click_images(driver,"lingzuan_02.1920x1080.png")
        # sleep(2)
        # driver(className="android.view.View",description='每日成功分享（0/1）').click()
        # #self.click_images(driver,"choujiang.1920x1080.png")
        # #self.click_images(driver,"lingzuian_05.1920x1080.png")
        # sleep(2)
        # driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=1).click()
        # self.click_images(driver,"lingzuan_02.1920x1080.png")
        # #sleep(2)
        # #driver(className="android.widget.LinearLayout",resourceId="com.tencent.mm:id/hf").click()
        # sleep(2)
        # driver(className="android.view.View",description='每日成功分享（0/1）').click()
        # #self.click_images(driver,"choujiang.1920x1080.png")
        # #self.click_images(driver,"lingzuian_06.1920x1080.png")
        # sleep(2)
        # driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=2).click()
        # sleep(2)
        # driver.press.back()
        # sleep(2)
        # driver(className="android.view.View",description='每日成功分享（0/1）').click()
        # self.click_images(driver,"lingzuan_01.1920x1080.png")
        # #sleep(2)
        # #driver(className="android.widget.GridViewt",index=0).child(className="android.widget.LinearLayout",index=3).click()
        # sleep(3)
        # driver.press.back()
        # sleep(2)
        # driver(className="android.view.View",description='每日成功分享（0/1）').click()
        # #self.click_images(driver,"choujiang.1920x1080.png")
        # #self.click_images(driver,"lingzuian_07.1920x1080.png")
        # sleep(2)
        # driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=4).click()
        # sleep(2)
        # driver.press.back()
        # driver.press.back()
        # sleep(1)
        # driver(className="android.widget.TextView",text="不保存").click()
        # driver(className="android.widget.ImageView", resourceId="com.crisisfire.android.nearme.gamecenter:id/uc_sdk_webviewtool_close_deufalt").click()
        # self.click_images(driver,"lingzuan_03.1920x1080.png")
        # #self.click_images(driver,"basic_16.1920x1080.png")
        sleep(1)
        driver.click(669,829)  # 领钻
        sleep(6)
        driver.click(1136,565)  # 立即抽奖
        sleep(2)
        driver.click(960,1000)  # 取消
        sleep(2)
        driver.click(1689,1020)  # 关闭
        sleep(2)
        if self.images_or_none(driver, 'basic_15.1920x1080.png'):
            return 'ok'
        else:
            return None
    
    def store(self,driver):
        # self.click_images(driver,"basic_17.1920x1080.png")
        # sleep(5)
        # driver(className="android.widget.ListView",index=0).child(className="android.view.View",index=1).click()
        # sleep(2)
        # driver(className="android.widget.ListView",index=0).child(className="android.view.View",index=2).click()
        # sleep(2)
        # driver(className="android.widget.ListView",index=0).child(className="android.view.View",index=3).click()
        # sleep(2)
        # driver(className="android.widget.ImageView", resourceId="com.crisisfire.android.nearme.gamecenter:id/uc_sdk_webviewtool_close_deufalt").click()
        # self.click_images(driver,"basic_18.1920x1080.png")
        sleep(1)
        driver.click(800,836)  # 神秘商店
        sleep(6)
        driver.click(80,350)  # 推荐
        sleep(2)
        driver.click(80,590)  # 积分商城
        sleep(2)
        driver.click(80,850)  # 订单
        sleep(2)
        driver.click(1690,1020)  # 关闭
        sleep(2)
        if self.images_or_none(driver, 'basic_15.1920x1080.png'):
            return 'ok'
        else:
            return None
        

    def talking(self,driver):
        # self.click_images(driver,"talking_01.1920x1080.png")
        # self.click_images(driver,"talking_02.1920x1080.png")
        sleep(1)
        driver.click(50,1015)  # 谈话
        sleep(2)
        driver.click(950,929)  # 点击对话框
        sleep(2)
        # driver(className='android.widget.EditText',index=0).click()
        driver.type(u"毛泽东法轮功江泽民")
        sleep(2)
        driver(className='android.widget.Button',index=1).click()
        sleep(2)
        driver.click(1600,929)  # 发送
        sleep(2)
        driver.click(1685,185)  # 关闭
        # self.click_images(driver,"talking_03.1920x1080.png")
        # self.click_images(driver,"talking_04.1920x1080.png")
        if self.wait_gone_images(driver, 'talking_exist.1920x1080.png'):
            return 'ok'
        else:
            return None
        
    def setting(self,driver):
        # self.click_images(driver,"setting.1920x1080.png")
        sleep(2)
        driver.long_click(1862,40)  # 设置
        # driver.long_click(1250,27)
        sleep(2)
        driver.click(1685,185)  # 关闭
        if self.wait_gone_images(driver, 'exists_01.1920x1080.png'):
            log.info('进入设置界面')
            return 'ok'
        else:
            return None
        
    def exitgame(self,driver):
        sleep(2)
        driver.long_click(1862,40)  # 设置
        sleep(2)
        driver.long_click(380,980)  # 退出游戏
        if self.wait_gone_images(driver, 'exit.1920x1080.png'):
            log.info('游戏中退出按钮')
            return 'ok'
        else:
            return None
        
        
        
        
        
    
        
        


