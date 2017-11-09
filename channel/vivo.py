# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'exists_02.1920x1080.png',way_name='channel'):
            sleep(2)
            driver(className="android.widget.EditText", resourceId="com.vivo.sdkplugin:id/account_num_input").click()
            driver.clear_text()
            driver.type("15198139230")
            driver(className="android.widget.EditText", resourceId="com.vivo.sdkplugin:id/account_password_input").click()
            driver.clear_text()
            driver.type("a123123")
            driver(className='android.widget.Button',index=1).click()
            self.click_images(driver,"shiming_close.1920x1080.png",way_name='channel')
            image = self.wait_gone_images(driver, 'exists_02.1920x1080.png',timeout=40,way_name='channel')
            if image:
                log.info('登录成功')
                return 'ok'
            else:
                log.info('登录失败')
                return None
        else:
            self.click_images(driver,"shiming_close.1920x1080.png",way_name='channel')
            image = self.wait_gone_images(driver, 'exists_02.1920x1080.png',way_name='channel')
            if image:
                log.info('自动登录成功')
                return 'ok'
    
    def fubiao(self,driver):
        u"浮标检查"
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_02.1920x1080.png",way_name='channel')
        driver(index=1, resourceId="com.vivo.sdkplugin:id/vivo_title_close_btn").click()
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_03.1920x1080.png",way_name='channel')
        sleep(1)
        driver(index=3, resourceId="com.vivo.sdkplugin:id/vivo_title_close_btn").click()
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        sleep(1)
        driver(index=3, resourceId="com.vivo.sdkplugin:id/vivo_title_close_btn").click()
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_05.1920x1080.png",way_name='channel')
        sleep(1)
        driver(index=1, resourceId="com.vivo.sdkplugin:id/vivo_title_close_btn").click()
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_06.1920x1080.png",way_name='channel')
        sleep(1)
        driver(index=1, resourceId="com.vivo.sdkplugin:id/vivo_title_close_btn").click()
        if self.wait_gone_images(driver, 'fubiao_06.1920x1080.png',way_name='channel'):
            log.info('浮标检查成功')
            return "OK"
        else:
            log.info('浮标检查失败')
            return None
        
    def ali(self,driver):
        u'''支付宝支付'''
        sleep(1)
        driver(className='android.widget.ListView',index=0).child(className='android.widget.RelativeLayout',index=1,clickable='true').click()
        driver(resourceId='com.vivo.sdkplugin:id/vivo_payment_btn_submit',index=3).click() #立即支付
        if self.images_or_none(driver, 'ali_pay_back.1920x1080.png',way_name='channel'):
            self.click_images(driver,"ali_pay_back.1920x1080.png",way_name='channel')
            self.click_images(driver,"ali_pay_back_yes.1920x1080.png",way_name='channel')
        else:
            driver.press.back()
        driver(resourceId='com.vivo.sdkplugin:id/vivo_payment_recharge_back',index=0).click()
        if self.wait_gone_images(driver, 'ali_pay_back.1920x1080.png',way_name='channel'):
            log.info('支付宝支付成功')
            return "OK"
        else:
            log.info('支付宝支付失败')
            return None
        
    def wechat(self,driver):
        u'''微信支付'''
        sleep(1)
        driver(className='android.widget.ListView',index=0).child(className='android.widget.RelativeLayout',index=0,clickable='true').click() #微信支付
        driver(resourceId='com.vivo.sdkplugin:id/vivo_payment_btn_submit',index=3).click()  #立即支付
        sleep(3)
        driver(className='android.widget.LinearLayout',index=0).child(className="android.widget.ImageView",index=0).click() #退出微信
        #driver(className='android.widget.RelativeLayout',index=0).child(className="android.widget.ImageView",index=0).click() #支付退出确定
        driver(resourceId='com.vivo.sdkplugin:id/vivo_payment_recharge_back',index=0).click()
        sleep(2)
        driver.press.back()
        driver(resourceId='com.vivo.sdkplugin:id/vivo_common_dlg_btn_positive',index=0).click()
        if self.wait_gone_images(driver, 'ali_pay_back.1920x1080.png',way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None
        
    def exitGame(self,driver):
        sleep(2)
        driver(resourceId='com.vivo.sdkplugin:id/vivo_app_exit_dialog_confirm_btn',index=0).click()
        if self.wait_gone_images(driver, 'ali_pay_back.1920x1080.png',way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None
       

