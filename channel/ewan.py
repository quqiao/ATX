# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def ewanUpdate(self,driver):
        self.click_images(driver,"ewanUpdate.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'ewanUpdate.1920x1080.png',way_name='channel'):
            log.info('更新提示关闭')
            return 'ok'
        else:
            return None
    
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'login_01.1920x1080.png',way_name='channel'):
            sleep(1)
            driver.click(680,700)  # 登录成功
            sleep(1)
            log.info('登录成功')
        else:
            log.info('自动登录完成')
        if self.wait_gone_images(driver, 'login_success.1920x1080.png',way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None

    def fubiao(self,driver):
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_02.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_03.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_05.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_06.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_06.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'fubiao_06.1920x1080.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None 
              

    def ali(self,driver):
        u"支付宝支付"
        self.click_images(driver,"ewan_pay_yes.1920x1080.png",way_name='channel')
        self.click_images(driver,"aliBack.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_exit_yes.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'ali_exit_yes.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
        
    def exitGame(self,driver):
        # self.click_exists(driver,"setting.1920x1080.png",way_name='channel')
        # self.click_exists(driver,"exitGame.1920x1080.png",way_name='channel')
        # self.click_exists(driver,"exitGame_01.1920x1080.png",way_name='channel')
        # self.click_exists(driver,"exitGame_02.1920x1080.png",way_name='channel')
        # self.click_exists(driver,"exitGame.1920x1080.png",way_name='channel')
        # self.click_exists(driver,"exitGame_01.1920x1080.png",way_name='channel')
        # self.click_exists(driver,"exitGame_03.1920x1080.png",way_name='channel')
        # sleep(1)
        # driver.click(600,930)  # 使用游戏方退出框
        # sleep(1)
        # driver.click(1200,720)  # 使用游戏方退出框
        # sleep(1)
        driver.click(1300,930)  # 直接退出
        sleep(1)
        if self.wait_gone_images(driver, 'exitGame_03.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None
            

        


