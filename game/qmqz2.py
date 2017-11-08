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
        sleep(20)
        #self.click_images(driver,"exit.1920x1080.png")
        #driver.start_app(configure.package_name,configure.activity_name)
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
        print '略过'
        if self.wait_gone_images(driver, 'exists_01.1920x1080.png'):
            return 'ok'
        else:
            return None 

       
    def guide(self,driver):
        '''引导第一次战斗'''
        if self.images_or_none(driver,'guide_001.1920x1080.png'):
            self.click_images(driver,"guide_001.1920x1080.png")
            self.click_images(driver,"guide_002.1920x1080.png")
            self.click_images(driver,"guide_003.1920x1080.png")
            self.click_images(driver,"guide_004.1920x1080.png")
            self.click_images(driver,"guide_005.1920x1080.png")
            self.click_images(driver,"guide_006.1920x1080.png")
            self.click_images(driver,"guide_007.1920x1080.png")
            self.click_images(driver,"guide_008.1920x1080.png")
            self.click_images(driver,"guide_009.1920x1080.png")
            self.click_images(driver,"guide_029.1920x1080.png")
            self.click_images(driver,"guide_010.1920x1080.png")
            self.click_images(driver,"guide_011.1920x1080.png")
            self.click_images(driver,"guide_012.1920x1080.png")
            '''商城'''
            sleep(10)
            driver.long_click(1819,989)
            driver.long_click(1209,658)
            sleep(1)
            driver.click(0.5,0.5)
            self.click_images(driver,"guide_013.1920x1080.png")
            self.click_images(driver,"guide_014.1920x1080.png")
            self.click_images(driver,"guide_015.1920x1080.png")
            self.click_images(driver,"guide_016.1920x1080.png")
            sleep(1)
            driver.click(0.5,0.5)
            '''装备'''
            sleep(1)
            driver.long_click(1869,45)
            driver.long_click(1243,30)
            self.click_images(driver,"guide_018.1920x1080.png")
            self.click_images(driver,"guide_019.1920x1080.png")
            self.click_images(driver,"guide_020.1920x1080.png")
            '''主页'''
            self.click_images(driver,"guide_021.1920x1080.png")
            sleep(1)
            driver.click(0.5,0.5)
            '''快速战斗'''
            self.click_images(driver,"guide_022.1920x1080.png")
            self.click_images(driver,"guide_023.1920x1080.png")
            self.click_images(driver,"guide_029.1920x1080.png")
            self.click_images(driver,"guide_024.1920x1080.png")
            self.click_images(driver,"guide_025.1920x1080.png")
            self.click_images(driver,"guide_026.1920x1080.png")
            '''关闭广告'''
            self.click_images(driver,"guide_027.1920x1080.png")
            self.click_images(driver,"guide_027.1920x1080.png")
            self.click_images(driver,"guide_028.1920x1080.png")
            self.click_images(driver,"guide_027.1920x1080.png")
            self.click_images(driver,"guide_027.1920x1080.png")
            self.click_images(driver,"guide_027.1920x1080.png")
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
        sleep(2)
        driver.long_click(1862,40)
        driver.long_click(1250,27)
        self.click_exists(driver,"huodong.1920x1080.png")
        for i in range(100):
            self.click_exists(driver,"huodong_close.1920x1080.png")
            if self.wait_gone_images(driver,"huodong_close.1920x1080.png",timeout=3):
                break
        self.click_images(driver,"basic_03.1920x1080.png")
        self.click_images(driver,"basic_04.1920x1080.png")
        self.click_images(driver,"basic_05.1920x1080.png")
        self.click_images(driver,"basic_06.1920x1080.png")
        self.click_images(driver,"basic_09.1920x1080.png")
        sleep(2)
        driver.long_click(1862,40)
        driver.long_click(1250,27)
        self.click_images(driver,"basic_19.1920x1080.png")
        sleep(2)
        driver.long_click(1862,40)
        driver.long_click(1250,27)
        self.click_images(driver,"basic_21.1920x1080.png")
        sleep(2)
        driver.long_click(1862,40)
        driver.long_click(1250,27)
        self.click_images(driver,"basic_23.1920x1080.png")
        sleep(2)
        driver.long_click(1862,40)
        driver.long_click(1250,27)
        self.click_images(driver,"basic_25.1920x1080.png")
        self.click_images(driver,"basic_26.1920x1080.png")
        self.click_images(driver,"basic_27.1920x1080.png")
        self.click_images(driver,"basic_28.1920x1080.png")
        sleep(2)
        driver.long_click(1862,40)
        driver.long_click(1250,27)
        self.click_images(driver,"basic_30.1920x1080.png")
        self.click_images(driver,"basic_31.1920x1080.png")
        self.click_images(driver,"basic_32.1920x1080.png")
        self.click_images(driver,"basic_33.1920x1080.png")
        self.click_images(driver,"basic_34.1920x1080.png")
        sleep(2)
        driver.long_click(1860,1000)
        driver.long_click(1210,660)
        sleep(2)
        driver.long_click(1820,40)
        driver.long_click(1250,27)
        self.click_images(driver,"basic_37.1920x1080.png")
        if self.images_or_none(driver, 'basic_03.1920x1080.png'):
            return 'ok'
        else:
            return None
    
    '''枪战直播'''   
    def live(self,driver):
        self.click_images(driver,"basic_07.1920x1080.png")
        self.click_images(driver,"live_01.1920x1080.png")
        self.click_images(driver,"live_02.1920x1080.png")
        #sleep(2)
        #driver(className="android.widget.RadioButton", resourceId="com.crisisfire.android.joloplay:id/usecenter_sdk_live_banner_close_tv").click()
        #driver(className="android.widget.RadioButton", resourceId="com.crisisfire.android.kp:id/usercenter_btn_live").click()
        self.click_images(driver,"basic_08.1920x1080.png")
        if self.images_or_none(driver, 'basic_07.1920x1080.png'):
            return 'ok'
        else:
            return None
    
    '''枪战攻略'''   
    def gonglue(self,driver):
        self.click_images(driver,"basic_11.1920x1080.png")
        self.click_images(driver,"gonglue_01.1920x1080.png")
        self.click_images(driver,"gonglue_02.1920x1080.png")
        self.click_images(driver,"gonglue_03.1920x1080.png")
        self.click_images(driver,"gonglue_04.1920x1080.png")
        
        '''
        sleep(5)
        driver(className="android.view.View",index=2).click() #红人
        driver(className="android.view.View",index=3).click() #攻略
        driver(className="android.view.View",index=4).click() #个人
        sleep(2)
        driver(className="android.widget.Button",descriptionContains=u"取消").click() #个人
        sleep(2)
        driver(className="android.widget.ImageView", resourceId="com.crisisfire.android.kp:id/uc_sdk_webviewtool_close_deufalt").click()
        #self.click_images(driver,"basic_12.1920x1080.png")
        '''
        if self.images_or_none(driver, 'basic_11.1920x1080.png'):
            return 'ok'
        else:
            return None
        
    
    '''枪战赛事'''    
    def saishi(self,driver):
        self.click_images(driver,"basic_13.1920x1080.png")
        sleep(5)
        #driver(className="android.view.View",index=0).child(className="android.view.View",index=0).click() 
        driver(className="android.widget.ListView",index=0).child(className="android.view.View",index=1).click() 
        driver(className="android.widget.ListView",index=0).child(className="android.view.View",index=2).click() 
        driver(className="android.widget.ListView",index=0).child(className="android.view.View",index=3).click() 
        #driver(className="android.widget.ImageView", resourceId="com.crisisfire.android.kp:id/uc_sdk_webviewtool_close_deufalt").click()
        self.click_images(driver,"basic_14.1920x1080.png")
        if self.images_or_none(driver, 'basic_13.1920x1080.png'):
            return 'ok'
        else:
            return None
       
    '''枪战领钻'''   
    def lingzuan(self,driver):
        self.click_images(driver,"basic_15.1920x1080.png")
        sleep(2)
        driver(className="android.view.View",description='每日成功分享（0/1）').click()
        #self.click_images(driver,"choujiang.1920x1080.png")
        #self.click_images(driver,"lingzuian_04.1920x1080.png")
        sleep(2)
        driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=0).click() 
        #sleep(3)
        #driver(className="android.widget.LinearLayout",resourceId="com.tencent.mm:id/hf").click()
        self.click_images(driver,"lingzuan_02.1920x1080.png")
        sleep(2)
        driver(className="android.view.View",description='每日成功分享（0/1）').click()
        #self.click_images(driver,"choujiang.1920x1080.png")
        #self.click_images(driver,"lingzuian_05.1920x1080.png")
        sleep(2)
        driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=1).click() 
        self.click_images(driver,"lingzuan_02.1920x1080.png")
        #sleep(2)
        #driver(className="android.widget.LinearLayout",resourceId="com.tencent.mm:id/hf").click()
        sleep(2)
        driver(className="android.view.View",description='每日成功分享（0/1）').click()
        #self.click_images(driver,"choujiang.1920x1080.png")
        #self.click_images(driver,"lingzuian_06.1920x1080.png")
        sleep(2)
        driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=2).click() 
        sleep(2)
        driver.press.back()
        sleep(2)
        driver(className="android.view.View",description='每日成功分享（0/1）').click()
        self.click_images(driver,"lingzuan_01.1920x1080.png")
        #sleep(2)
        #driver(className="android.widget.GridViewt",index=0).child(className="android.widget.LinearLayout",index=3).click() 
        sleep(3)
        driver.press.back()
        sleep(2)
        driver(className="android.view.View",description='每日成功分享（0/1）').click()
        #self.click_images(driver,"choujiang.1920x1080.png")
        #self.click_images(driver,"lingzuian_07.1920x1080.png")
        sleep(2)
        driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=4).click()  
        sleep(2)
        driver.press.back()
        driver.press.back()
        sleep(1)
        driver(className="android.widget.TextView",text="不保存").click()
        #driver(className="android.widget.ImageView", resourceId="com.crisisfire.android.nearme.gamecenter:id/uc_sdk_webviewtool_close_deufalt").click()
        self.click_images(driver,"lingzuan_03.1920x1080.png")
        #self.click_images(driver,"basic_16.1920x1080.png")
        if self.images_or_none(driver, 'basic_15.1920x1080.png'):
            return 'ok'
        else:
            return None
    
    def store(self,driver):
        self.click_images(driver,"basic_17.1920x1080.png")
        sleep(5)
        driver(className="android.widget.ListView",index=0).child(className="android.view.View",index=1).click()
        sleep(2)
        driver(className="android.widget.ListView",index=0).child(className="android.view.View",index=2).click()
        sleep(2)
        driver(className="android.widget.ListView",index=0).child(className="android.view.View",index=3).click() 
        #sleep(2)
        #driver(className="android.widget.ImageView", resourceId="com.crisisfire.android.nearme.gamecenter:id/uc_sdk_webviewtool_close_deufalt").click()
        self.click_images(driver,"basic_18.1920x1080.png")
        if self.images_or_none(driver, 'basic_15.1920x1080.png'):
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

        if self.wait_gone_images(driver, 'talking_exist.1920x1080.png'):
            return 'ok'
        else:
            return None
        
    def setting(self,driver):
        #self.click_images(driver,"setting.1920x1080.png")
        sleep(2)
        driver.long_click(1862,40)
        driver.long_click(1250,27)
        if self.wait_gone_images(driver, 'exists_01.1920x1080.png'):
            log.info('进入设置界面')
            return 'ok'
        else:
            return None
        
    def exitgame(self,driver):
        self.click_images(driver,"exit_game.1920x1080.png")
        if self.wait_gone_images(driver, 'exit.1920x1080.png'):
            log.info('游戏中退出按钮')
            return 'ok'
        else:
            return None
        
        
        
        
        
    
        
        


