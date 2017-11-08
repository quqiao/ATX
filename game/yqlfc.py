#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)
import threading

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
        self.click_images(driver,"game_pre_02.1920x1080.png")
        if self.wait_gone_images(driver,'game_pre_02.1920x1080.png'):
            log.info('进入游戏前准备成功')
            return 'ok'
        else:
            log.info('进入游戏前准备失败')
            return None
        
    def guide(self,driver):
        '''引导开始'''
        if self.images_or_none(driver,'guide_002.1920x1080.png'):
            self.click_images(driver,"guide_001.1920x1080.png")
            self.click_images(driver,"guide_002.1920x1080.png")
            sleep(8)
            self.images_or_none(driver,'guide_003.1920x1080.png')
            driver.click(0.5,0.5)
            sleep(2)
            self.images_or_none(driver,'guide_003.1920x1080.png')
            driver.click(0.5,0.5)
            '''右转'''
            sleep(5)
            driver.swipe(1000,500,1000,500,40)
            sleep(5)
            '''左转'''
            driver.swipe(400,500,400,500,40)
            self.images_or_none(driver,'guide_003.1920x1080.png')
            driver.click(0.5,0.5)
            sleep(2)
            self.images_or_none(driver,'guide_003.1920x1080.png')
            driver.click(0.5,0.5)
            sleep(3)
            '''左漂移'''
            def long1():
                driver.click(400,500)
            def long2():
                driver.click(1000,500)
            def long3():
                driver.click(1000,500)
            def long4():
                driver.click(400,500)
            threads = []
            t1 = threading.Thread(target=long1)
            threads.append(t1)
            t2 = threading.Thread(target=long2)
            threads.append(t2)
            sleep(1)
            for t in threads:
                t.start()
            threads1 = []
            t3 = threading.Thread(target=long3)
            threads.append(t3)
            t4 = threading.Thread(target=long4)
            threads.append(t4)
            sleep(1)
            for t in threads1:
                t.start()
            threads2 = []
            t1 = threading.Thread(target=long1)
            threads1.append(t1)
            t2 = threading.Thread(target=long2)
            threads1.append(t2)
            for t in threads2:
                t.start()
            sleep(1)
            threads3 = []
            t3 = threading.Thread(target=long3)
            threads1.append(t3)
            t4 = threading.Thread(target=long4)
            threads1.append(t4)
            for t in threads3:
                t.start()
            sleep(1)
            threads4 = []
            t3 = threading.Thread(target=long1)
            threads2.append(t3)
            t4 = threading.Thread(target=long2)
            threads2.append(t4)
            t5 = threading.Thread(target=long3)
            threads2.append(t5)
            t6 = threading.Thread(target=long4)
            threads2.append(t6)
            for t in threads2:
                t.start()
            sleep(2)
            driver.long_click(400,500)
            sleep(8)
            '''右漂移'''
            #for i in range(2):
                #self.images_or_none(driver,'guide_003.1920x1080.png')
                #driver.click(0.5,0.5)
            
            threads = []
            t1 = threading.Thread(target=long1)
            threads.append(t1)
            t2 = threading.Thread(target=long2)
            threads.append(t2)
            t3 = threading.Thread(target=long3)
            threads.append(t3)
            t4 = threading.Thread(target=long4)
            threads.append(t4)
            for t in threads:
                t.start()
            sleep(1)
            threads1 = []
            t1 = threading.Thread(target=long1)
            threads1.append(t1)
            t2 = threading.Thread(target=long2)
            threads1.append(t2)
            t3 = threading.Thread(target=long3)
            threads1.append(t3)
            t4 = threading.Thread(target=long4)
            threads1.append(t4)
            for t in threads1:
                t.start()
            sleep(1)
            threads2 = []
            t3 = threading.Thread(target=long1)
            threads2.append(t3)
            t4 = threading.Thread(target=long2)
            threads2.append(t4)
            t5 = threading.Thread(target=long3)
            threads2.append(t5)
            t6 = threading.Thread(target=long4)
            threads2.append(t6)
            for t in threads2:
                t.start()
            sleep(2)
            driver.long_click(1000,500)
            '''氮气'''
            self.click_images(driver,"guide_004.1920x1080.png")
            self.images_or_none(driver,'guide_003.1920x1080.png')
            driver.click(0.5,0.5)
            '''设置'''
            self.click_images(driver,"guide_005.1920x1080.png")
            self.click_images(driver,"guide_006.1920x1080.png")
            self.click_images(driver,"guide_007.1920x1080.png")
            self.images_or_none(driver,'guide_003.1920x1080.png')
            sleep(2)
            driver.click(0.5,0.5)
            '''任务'''
            self.images_or_none(driver,'guide_008.1920x1080.png')
            driver.swipe(1846,597,1846,597,10)
            driver.swipe(1230,393,1230,393,10)
            #self.click_images(driver,"guide_008.1920x1080.png")
            self.click_images(driver,"guide_009.1920x1080.png")
            self.click_images(driver,"guide_010.1920x1080.png")
            driver.click(0.5,0.5)
            self.click_images(driver,"guide_011.1920x1080.png")
            self.click_images(driver,"guide_012.1920x1080.png")
            self.click_images(driver,"guide_013.1920x1080.png")
            self.click_images(driver,"guide_014.1920x1080.png")
            '''开始游戏'''
            self.images_or_none(driver,'guide_003.1920x1080.png')
            driver.click(0.5,0.5)
            self.click_images(driver,"guide_015.1920x1080.png")
            self.click_images(driver,"guide_016.1920x1080.png")
            self.click_images(driver,"guide_017.1920x1080.png")
            self.click_images(driver,"guide_017.1920x1080.png")
        
        else:
            driver.click(0.5,0.5)
            self.click_images(driver,"guide_015.1920x1080.png")
            self.click_images(driver,"guide_016.1920x1080.png")
            self.click_images(driver,"guide_017.1920x1080.png")
            self.click_images(driver,"guide_017.1920x1080.png") 
        if self.wait_gone_images(driver,'guide_017.1920x1080.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
        

    def basicFunction(self,driver):
        self.click_images(driver,"basic_001.1920x1080.png")
        self.click_images(driver,"basic_002.1920x1080.png")
        self.click_images(driver,"basic_003.1920x1080.png")
        self.click_images(driver,"basic_004.1920x1080.png")
        self.click_images(driver,"basic_005.1920x1080.png")
        self.click_images(driver,"basic_004.1920x1080.png")
        self.click_images(driver,"basic_006.1920x1080.png")
        self.click_images(driver,"basic_007.1920x1080.png")
        self.click_images(driver,"basic_004.1920x1080.png")
        self.click_images(driver,"basic_008.1920x1080.png")
        self.click_images(driver,"basic_009.1920x1080.png")
        self.click_images(driver,"basic_010.1920x1080.png")
        self.click_images(driver,"basic_011.1920x1080.png")
        self.click_images(driver,"basic_012.1920x1080.png")
        self.click_images(driver,"basic_004.1920x1080.png")
        self.click_images(driver,"basic_013.1920x1080.png")
        self.click_images(driver,"basic_004.1920x1080.png")
        self.click_images(driver,"basic_014.1920x1080.png")
        self.click_images(driver,"basic_002.1920x1080.png")
        if self.wait_gone_images(driver, 'basic_002.1920x1080.png'):
            return 'ok'
        else:
            return None
        
    '''飞车祈福'''   
    def live(self,driver):
        self.click_images(driver,"live_001.1920x1080.png")
        self.click_images(driver,"live_002.1920x1080.png")
        if self.wait_gone_images(driver, 'live_002.1920x1080.png'):
            return 'ok'
        else:
            return None
        
    '''飞车社区'''   
    def gonglue(self,driver):
        self.click_images(driver,"gonglue_01.1920x1080.png")
        self.click_images(driver,"gonglue_02.1920x1080.png")
        self.click_images(driver,"gonglue_03.1920x1080.png")
        self.click_images(driver,"gonglue_04.1920x1080.png")
        self.click_images(driver,"gonglue_05.1920x1080.png")
        if self.wait_gone_images(driver, 'gonglue_01.1920x1080.png'):
            return 'ok'
        else:
            return None
        
    '''飞车特惠 '''
    def store(self,driver):
        driver.swipe(1846,785,1846,785,10)
        driver.swipe(1230,520,1230,520,10)
        self.click_images(driver,"store_02.1920x1080.png")
        if self.wait_gone_images(driver, 'store_02.1920x1080.png'):
            return 'ok'
        else:
            return None
        
    '''飞车邀请'''   
    def lingzuan(self,driver):
        driver.swipe(1846,230,1846,230,10)
        driver.swipe(1230,150,1230,150,10)
        sleep(2)
        driver(className="android.view.View",description='每日成功分享（0/1）').click()
        self.click_images(driver,"lingzuan_04.1920x1080.png")
        sleep(2)
        driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=0).click() 
        self.click_images(driver,"lingzuan_02.1920x1080.png")
        sleep(2)
        driver(className="android.view.View",description='每日成功分享（0/1）').click()
        self.click_images(driver,"lingzuan_04.1920x1080.png")
        sleep(2)
        driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=1).click() 
        self.click_images(driver,"lingzuan_02.1920x1080.png")
        sleep(2)
        driver(className="android.view.View",description='每日成功分享（0/1）').click()
        self.click_images(driver,"lingzuan_04.1920x1080.png")
        sleep(2)
        driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=2).click() 
        sleep(2)
        driver.press.back()
        sleep(2)
        driver(className="android.view.View",description='每日成功分享（0/1）').click()
        self.click_images(driver,"lingzuan_04.1920x1080.png")
        self.click_images(driver,"lingzuan_01.1920x1080.png")
        sleep(3)
        driver.press.back()
        sleep(2)
        driver(className="android.view.View",description='每日成功分享（0/1）').click()
        self.click_images(driver,"lingzuan_04.1920x1080.png")
        sleep(2)
        driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=4).click()  
        sleep(2)
        driver.press.back()
        driver.press.back()
        sleep(1)
        driver(className="android.widget.TextView",text="不保存").click()
        self.click_images(driver,"lingzuan_03.1920x1080.png")
        if self.wait_gone_images(driver, 'lingzuan_03.1920x1080.png'):
            return 'ok'
        else:
            return None

    '''飞车任务'''    
    def saishi(self,driver):
        driver.swipe(1846,597,1846,597,10)
        driver.swipe(1230,393,1230,393,10)
        self.click_images(driver,"saishi_02.1920x1080.png") 
        self.click_images(driver,"saishi_03.1920x1080.png") 
        self.click_images(driver,"saishi_04.1920x1080.png") 
        self.click_images(driver,"saishi_05.1920x1080.png") 
        self.click_images(driver,"saishi_06.1920x1080.png") 
        self.click_images(driver,"saishi_07.1920x1080.png") 
        if self.wait_gone_images(driver, 'saishi_07.1920x1080.png'):
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
        sleep(1)
        driver.click(1170,115)
        self.click_images(driver,"setting_02.1920x1080.png")
        if self.wait_gone_images(driver, 'setting_02.1920x1080.png'):
            log.info('游戏中退出按钮')
            return 'ok'
        else:
            return None
        
        
    def exitgame(self,driver):
        driver.press.back()
        self.click_images(driver,"exitgame_01.1920x1080.png")
        if self.wait_gone_images(driver, 'exitgame_01.1920x1080.png'):
            log.info('游戏中退出按钮')
            return 'ok'
        else:
            return None
