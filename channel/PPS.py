# coding=utf-8


from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'idInput.1920x1080.png',way_name='channel'):
            self.click_images(driver,u"idInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("18583238812") 
            self.click_images(driver,u"pswInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("qatest123")
            self.click_images(driver,u"login.1920x1080.png",way_name='channel')
        else:
            log.info('自动登录成功')
        if self.wait_gone_images(driver, 'login.1920x1080.png',way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None
            
    def fubiao(self,driver):
        self.click_exists(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_02.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_03.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_04.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_03.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_05.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_03.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_06.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_03.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_07.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_03.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'fubiao_03.1920x1080.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None 
        

    def ali(self,driver):
        u"支付宝支付"
        
        self.click_images(driver,"ali.1920x1080.png",way_name='channel')
        self.click_images(driver,"PPS_pay_certain.1920x1080.png",way_name='channel')
        sleep(2)
        self.click_images(driver,"aliBack.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_exit_yes.1920x1080.png",way_name='channel')
        self.click_images(driver,"pps_pay_fail_yes.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None   
    
        
    def wechat(self,driver):
        u"微信支付"
        self.click_images(driver,"PPS_pay_certain.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_Back.1920x1080.png",way_name='channel')
        self.click_images(driver,"pps_pay_fail_yes.1920x1080.png",way_name='channel')
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
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
    
    def mo9(self,driver): 
        u"mo9支付"
        self.click_images(driver,"mo9.1920x1080.png",way_name='channel')
        self.click_images(driver,"PPS_pay_certain.1920x1080.png",way_name='channel')
        self.click_images(driver,"mo9_close.1920x1080.png",way_name='channel')
        self.click_images(driver,"PPS_return_game.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None    

    def caifutong(self,driver): 
        u"财付通支付"
        self.click_images(driver,"caifutong.1920x1080.png",way_name='channel')
        self.click_images(driver,"PPS_pay_certain.1920x1080.png",way_name='channel')
        self.click_images(driver,"caifutong_close.1920x1080.png",way_name='channel')
        self.click_images(driver,"PPS_return_game.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def unionPay(self,driver): 
        u"财付通支付"
        self.click_images(driver,"unionPay    .1920x1080.png",way_name='channel')
        self.click_images(driver,"PPS_pay_certain.1920x1080.png",way_name='channel')
        self.click_images(driver,"caifutong_close.1920x1080.png",way_name='channel')
        self.click_images(driver,"PPS_return_game.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
        
    def exitGame(self,driver):
        self.click_exists(driver,"exitGame_02.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'exitGame_02.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None
            

