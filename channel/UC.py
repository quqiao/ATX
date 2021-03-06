# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'login_01.1920x1080.png',way_name='channel'):
            if self.images_or_none(driver, 'login_02.1920x1080.png',way_name='channel'):
                sleep(1)
                driver.click(880,700)  # 登录按钮
            else:
                # elf.click_images(driver,"idInput.1920x1080.png",way_name='channel')
                driver.click(505,868)  # 切换登录方式
                sleep(2)
                driver.click(505,868)  # 切换登录方式
                sleep(2)
                driver.click(800,380)  # 点击用户输入框
                sleep(1)
                driver.clear_text()
                sleep(1)
                driver.type("15202828543",next='True')
                sleep(1)
                driver.type("menglong")
                sleep(1)
                driver.click(880,700)  # 登录按钮
                sleep(5)
                driver.click(1359,150)  # 关闭实名
                # self.click_images(driver,"login.1920x1080.png",way_name='channel')
                # self.click_images(driver,"login_shiming_close.1920x1080.png",way_name='channel')

        else:
            # self.click_images(driver,"login_shiming_close.1920x1080.png",way_name='channel')
            sleep(2)
            driver.click(1359,150)  # 关闭实名
            log.info('自动登录成功')

        if self.wait_gone_images(driver, 'login_success.1920x1080.png',way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None
    
    def fubiao(self,driver):
        sleep(1)
        driver.swipe(15,190,960,920,50)
        sleep(2)
        driver.click(1115,860)  # 隐藏
        log.info('移动浮标隐藏')
        # self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_02.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_03.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_05.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_06.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_07.1920x1080.png",way_name='channel')
        sleep(2)
        driver.swipe(20,355,960,909)
        self.click_images(driver,"fubiao_08.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'fubiao_01.1920x1080.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None            
    
    def ali(self,driver):
        u"支付宝支付"
        sleep(2)
        self.click_images(driver,"UC_change_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali.1920x1080.png",way_name='channel')
        self.click_images(driver,"UC_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"aliBack.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_exit_yes.1920x1080.png",way_name='channel')
        self.click_images(driver,"uc_pay_fail_back.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    
        
    def wechat(self,driver):
        u"微信支付"
        sleep(2)
        self.click_images(driver,"UC_change_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat.1920x1080.png",way_name='channel')
        self.click_images(driver,"UC_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_Back.1920x1080.png",way_name='channel')
        self.click_images(driver,"uc_pay_fail_back.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def yinhangka(self,driver): 
        u"银行卡支付"
        self.click_images(driver,"yinhangka.1920x1080.png",way_name='channel')
        self.click_images(driver,"PPS_pay_certain.1920x1080.png",way_name='channel')
        self.click_images(driver,"yinhangka_close.1920x1080.png",way_name='channel')
        self.click_images(driver,"yinhangka_close_yes.1920x1080.png",way_name='channel')
        self.click_images(driver,"pps_pay_fail_yes.1920x1080.png",way_name='channel')
    
    def mo9(self,driver): 
        u"mo9支付"
        self.click_images(driver,"mo9.1920x1080.png",way_name='channel')
        self.click_images(driver,"PPS_pay_certain.1920x1080.png",way_name='channel')
        self.click_images(driver,"mo9_close.1920x1080.png",way_name='channel')
        self.click_images(driver,"PPS_return_game.1920x1080.png",way_name='channel')      

    def caifutong(self,driver): 
        u"财付通支付"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"caifutong.1920x1080.png",way_name='channel')
            self.click_images(driver,"PPS_pay_certain.1920x1080.png",way_name='channel')
            self.click_images(driver,"caifutong_close.1920x1080.png",way_name='channel')
            self.click_images(driver,"PPS_return_game.1920x1080.png",way_name='channel')
            
    def unionPay(self,driver): 
        u"财付通支付"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"unionPay    .1920x1080.png",way_name='channel')
            self.click_images(driver,"PPS_pay_certain.1920x1080.png",way_name='channel')
            self.click_images(driver,"caifutong_close.1920x1080.png",way_name='channel')
            self.click_images(driver,"PPS_return_game.1920x1080.png",way_name='channel')
            
    def exitGame(self,driver):
        # self.click_images(driver,"setting.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_01.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_02.1920x1080.png",way_name='channel')
        sleep(2)
        driver.click(790,710)
        if self.wait_gone_images(driver, 'exitGame_02.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None
