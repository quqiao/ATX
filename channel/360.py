#!/usr/bin/env python
# coding=utf-8

import public.methods as public
from time import sleep
from public import logutils
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'exists_03.1920x1080.png',way_name='channel'):
            '''
            self.click_images(driver,"idInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("15198139230") 
            self.click_images(driver,"pswInput.1920x1080.png",way_name='channel',timeout=40)
            sleep(1)
            driver.type("a123123")
            self.click_images(driver,"login.1920x1080.png",way_name='channel')
            self.click_images(driver,"login_bangding_back.1920x1080.png",way_name='channel')
            self.click_images(driver,"login_shiming_close.1920x1080.png",way_name='channel')
            '''
            # driver(className="android.widget.EditText").sibling(className="android.widget.ImageView").click()
            sleep(2)
            driver.click(850,230)  # 登录
            sleep(1)
            driver.clear_text()
            sleep(1)
            driver.type("15198139230",next=True)
            sleep(1)
            driver.type("a123123")
            sleep(1)
            driver.click(950,610)
            # driver(className="android.widget.Button",index=0).sibling(className="android.widget.LinearLayout",index=1).click()
            image = self.wait_gone_images(driver, 'login_shiming_close.1920x1080.png',timeout=40,way_name='channel')
            if image:
                log.info('登录成功')
                return 'ok'
            else:
                log.info('登录失败')
                return None

        else:
            self.click_images(driver,"login_bangding_back.1920x1080.png",way_name='channel')
            self.click_images(driver,"login_shiming_close.1920x1080.png",way_name='channel')
            image = self.wait_gone_images(driver, 'login_shiming_close.1920x1080.png',way_name='channel')
            if image:
                log.info('自动登录成功')
                return 'ok'
            
    def fubiao(self,driver):
        u'浮标操作'
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_02.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_03.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_05.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_06.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_07.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_08.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_09.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'fubiao_01.1920x1080.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None


    def ali(self,driver):
        u"支付宝支付"
        self.click_images(driver,"close_shiming.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali.1920x1080.png",way_name='channel')
        self.click_images(driver,"alipay.1920x1080.png",way_name='channel')
        ##########不支付退出#######################
        self.click_images(driver,"aliBack.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_exit_yes.1920x1080.png",way_name='channel')
        self.click_images(driver,"pay_fail_yes.1920x1080.png",way_name='channel')
        '''
        ###########登录支付宝账号################
        if self.images_or_none(driver, 'exists_alipay01.1920x1080.png',way_name='channel'):
            for i in range(10):
                self.click_images(driver,"alipay_login01.1920x1080.png",way_name='channel')
                if self.wait_gone_images(driver,"alipay_login01.1920x1080.png",way_name='channel'):
                    break
            self.click_images(driver,"alipay_login02.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("18583762260")
            self.click_images(driver,"alipay_login03.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("687411")
            self.click_images(driver,"alipay_login04.1920x1080.png",way_name='channel')
            self.click_images(driver,"alipay_login05.1920x1080.png",way_name='channel')
            self.click_images(driver,"alipay_login06.1920x1080.png",way_name='channel')
            self.click_images(driver,"alipay_login07.1920x1080.png",way_name='channel')
        ###########已支付过再用支付宝支付################
        if self.images_or_none(driver, 'alipay_login05.1920x1080.png',way_name='channel'):
            self.click_images(driver,"alipay_login05.1920x1080.png",way_name='channel')
            self.click_images(driver,"alipay_login06.1920x1080.png",way_name='channel')
            self.click_images(driver,"alipay_login07.1920x1080.png",way_name='channel')
        '''
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            log.info('支付宝检查完成')
            return 'ok'
        else:
            return None
        

    def wechat(self,driver):
        u"微信支付"
        self.click_images(driver,"close_shiming.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_pay.1920x1080.png",way_name='channel')
        ############微信不支付#################
        self.click_images(driver,"wechat_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"pay_fail_yes.1920x1080.png",way_name='channel')
        ################登录微信#####################
        '''
        if self.images_or_none(driver, 'wechatpay_login03.1920x1080.png',way_name='channel'):
            self.click_images(driver,"wechatpay_login01.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("18583762260")
            self.click_images(driver,"wechatpay_login02.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("qatest2017")
            self.click_images(driver,"wechatpay_login03.1920x1080.png",way_name='channel')
            self.click_images(driver,"wechatpay_login04.1920x1080.png",way_name='channel')
            self.click_images(driver,"wechatpay_login05.1920x1080.png",way_name='channel')
            self.click_images(driver,"wechatpay_login06.1920x1080.png",way_name='channel')
            self.click_images(driver,"wechatpay_login07.1920x1080.png",way_name='channel')
            self.click_images(driver,"wechatpay_login08.1920x1080.png",way_name='channel')
            self.click_images(driver,"wechatpay_login09.1920x1080.png",way_name='channel')
            self.click_images(driver,"wechatpay_login09.1920x1080.png",way_name='channel')
            self.click_images(driver,"wechatpay_login10.1920x1080.png",way_name='channel')
            sleep(2)
            driver.keyevent('BACK')
            self.click_images(driver,"wechatpay_login12.1920x1080.png",way_name='channel')
            self.click_images(driver,"wechat_back.1920x1080.png",way_name='channel')
            self.click_images(driver,"wechatpay_login11.1920x1080.png",way_name='channel')
            for i in xrange(10):
                self.click_images(driver,"pay_01.1920x1080.png")
                sleep(2)
                if self.exist(driver,'exists_01.1920x1080.png'):
                    print 'fail'
                    break
            if self.images_or_none(driver, 'exists_01.1920x1080.png'):
                return 'ok'
            else:
                return None 
        if self.images_or_none(driver, 'wechatpay_login04.1920x1080.png',way_name='channel'):
            self.click_images(driver,"wechatpay_login04.1920x1080.png",way_name='channel')
            self.click_images(driver,"wechatpay_login05.1920x1080.png",way_name='channel')
            self.click_images(driver,"wechatpay_login06.1920x1080.png",way_name='channel')
            self.click_images(driver,"wechatpay_login07.1920x1080.png",way_name='channel')
            self.click_images(driver,"wechatpay_login08.1920x1080.png",way_name='channel')
            self.click_images(driver,"wechatpay_login09.1920x1080.png",way_name='channel')
            self.click_images(driver,"wechatpay_login09.1920x1080.png",way_name='channel')
            self.click_images(driver,"wechatpay_login10.1920x1080.png",way_name='channel')
            sleep(2)
            driver.keyevent('BACK')
            self.click_images(driver,"wechatpay_login12.1920x1080.png",way_name='channel')
            self.click_images(driver,"wechatpay_login11.1920x1080.png",way_name='channel')
            for i in xrange(10):
                self.click_images(driver,"pay_01.1920x1080.png")
                sleep(2)
                if self.exist(driver,'exists_01.1920x1080.png'):
                    print 'fail'
                    break
            if self.images_or_none(driver, 'exists_01.1920x1080.png'):
                return 'ok'
            else:
                return None 
        '''
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            log.info('微信检查完成')
            return 'ok'
        else:
            return None
        
        
    def exitGame(self,driver):
        # self.click_images(driver,"exitGame_01.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_02_close.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_01.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_01_huodong.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_01_huodong_close.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_01.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_02.1920x1080.png",way_name='channel')
        driver.click(685,720)  # 退出游戏
        if self.wait_gone_images(driver, 'exitGame_02.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None
        
        

