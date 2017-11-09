#!/usr/bin/env python
# coding=utf-8


from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, u'idInput.1920x1080.png',way_name='channel'):
            self.click_images(driver,"idInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.clear_text()
            sleep(1)
            driver.type("wan279378792", next=True) 
            # self.click_images(driver,"pswInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.clear_text()
            sleep(1)
            driver.type("981298")
            self.click_images(driver,"login.1920x1080.png",way_name='channel')

        else:
            self.wait_gone_images(driver, 'login.1920x1080.png',timeout=40,way_name='channel')
            log.info('自动登录成功')

        if self.wait_gone_images(driver, 'login.1920x1080.png',timeout=40,way_name='channel'):
                log.info('登录成功')
                return 'ok'
        else:
            log.info('登录失败')
            return None
            
    def fubiao(self,driver):
        u'浮标操作'
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_02.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_03.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_05.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_06.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_05.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_07.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_08.1920x1080.png",way_name='channel')
        for i in xrange(10):
                self.click_images(driver,"fubiao_09.1920x1080.png",way_name='channel')
                sleep(1)
                if self.exist(driver,'exists_qmqz.1920x1080.png',way_name='channel'):
                    print 'fail'
                    break
        if self.wait_gone_images(driver, 'fubiao_09.1920x1080.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None          

    def exitGame(self,driver):
        log.info('没有内容')
        if self.wait_gone_images(driver, 'fubiao_09.1920x1080.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None

    def ali(self,driver):
        u"支付宝支付"
        self.click_images(driver,"37_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali.1920x1080.png",way_name='channel')
        self.click_images(driver,"aliBack.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_exit_yes.1920x1080.png",way_name='channel')
        self.click_images(driver,"37_return_game.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None

    def wangshangyinhang(self,driver):
        u"网上银行"
        self.click_images(driver,"37_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"wangshangyinhang.1920x1080.png",way_name='channel')
        self.click_images(driver,"aliBack.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_exit_yes.1920x1080.png",way_name='channel')
        self.click_images(driver,"37_return_game.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def unionPay(self,driver): 
        u"银联卡"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"37_pay.1920x1080.png",way_name='channel')
            self.click_images(driver,"unionPay.1920x1080.png",way_name='channel')
            self.click_images(driver,"unionPay_cancel.1920x1080.png",way_name='channel')

    def CreditPay(self,driver): 
        u"信用卡"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"37_pay.1920x1080.png",way_name='channel')
            self.click_images(driver,"CreditPay.1920x1080.png",way_name='channel')  
            self.click_images(driver,"unionPay_cancel.1920x1080.png",way_name='channel')
            
    def caifutong(self,driver): 
        u"财付通"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"37_pay.1920x1080.png",way_name='channel')
            self.click_images(driver,"caifutong.1920x1080.png",way_name='channel')
            self.click_images(driver,"pay_return_game.1920x1080.png",way_name='channel')
            
    def zhuanzhang(self,driver):
        u"转账汇款"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"37_pay.1920x1080.png",way_name='channel')
            self.click_images(driver,"zhuanzhang.1920x1080.png",way_name='channel')
            self.click_images(driver,"pay_return_game.1920x1080.png",way_name='channel')
            
    def chinaMobile(self,driver):
        u"中国移动"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"37_pay.1920x1080.png",way_name='channel')
            self.click_images(driver,"chinaMobile.1920x1080.png",way_name='channel')
            self.click_images(driver,"pay_return_game.1920x1080.png",way_name='channel')
        
    def chinaUnicom(self,driver):
        u"中国联通"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"37_pay.1920x1080.png",way_name='channel')
            self.click_images(driver,"chinaUnicom.1920x1080.png",way_name='channel')
            self.click_images(driver,"pay_return_game.1920x1080.png",way_name='channel')
            
    def chinaTelecom(self,driver):
        u"中国电信"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"37_pay.1920x1080.png",way_name='channel')
            self.click_images(driver,"chinaTelecom.1920x1080.png",way_name='channel')
            self.click_images(driver,"pay_return_game.1920x1080.png",way_name='channel')
            
    def junwang(self,driver):
        u"骏卡"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"37_pay.1920x1080.png",way_name='channel')
            self.click_images(driver,"junwang.1920x1080.png",way_name='channel')
            self.click_images(driver,"pay_return_game.1920x1080.png",way_name='channel')

