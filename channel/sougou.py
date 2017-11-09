# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'idInput.1920x1080.png',way_name='channel'):
            self.click_images(driver,"idInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("sg774988pgq") 
            self.click_images(driver,"pswInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("123456")
            self.click_images(driver,"login.1920x1080.png",way_name='channel')
            self.click_images(driver,"login_shiming_close.1920x1080.png",way_name='channel')
        else:
            self.click_images(driver,"login_shiming_close.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'login_shiming_close.1920x1080.png',way_name='channel'):
                log.info('登录成功')
                return 'ok'
        else:
            log.info('登录失败')
            return None
    
    def fubiao(self,driver):
        '''
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_02.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_03.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_06.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_03.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_06.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_05.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_07.1920x1080.png",way_name='channel')
        '''
        sleep(2)
        driver.click(1898,285)#浮标
        sleep(2)
        driver.click(1669,285)#新游
        sleep(2)
        driver.click(1749,113)#关闭
        sleep(2)
        driver.click(1898,285)#浮标
        sleep(2)
        driver.click(1550,285)#福利
        sleep(2)
        driver.click(1749,113)#关闭
        sleep(2)
        driver.click(1898,285)#浮标
        sleep(2)
        driver.click(1420,285)#我的
        sleep(2)
        driver.click(1780,100)#关闭
        sleep(2)
        if self.wait_gone_images(driver, 'fubiao_07.1920x1080.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None           
    
    def ali(self,driver):
        u"支付宝支付"
        
        self.click_images(driver,"sougou_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_pay_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_pay_back_yes.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def wechat(self,driver):
        u"微信支付"
        
        self.click_images(driver,"wechat.1920x1080.png",way_name='channel')
        self.click_images(driver,"sougou_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_back.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
        
    def exitGame(self,driver):
        self.click_images(driver,"exitGame_01.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'exitGame_01.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None
    

