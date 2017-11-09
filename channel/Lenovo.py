# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'exists_02.1920x1080.png',way_name='channel'):
            driver(className='android.widget.RelativeLayout',index=0).child(className='android.widget.RelativeLayout',index=0).click()
            driver.clear_text()
            driver.type("18482311990")
            driver(className='android.widget.RelativeLayout',index=0).child(className='android.widget.RelativeLayout',index=2).click()
            driver.clear_text()
            driver.type("123456")
            driver(className='android.widget.LinearLayout',index=2).child(className='android.widget.Button',index=1).click()
            image = self.wait_gone_images(driver, 'exists_02.1920x1080.png',timeout=40,way_name='channel')
            if image:
                log.info('登录成功')
                return 'ok'
            else:
                log.info('登录失败')
                return None
        else:
            image = self.wait_gone_images(driver, 'exists_02.1920x1080.png',way_name='channel')
            if image:
                log.info('自动登录成功')
                return 'ok'
    
    def fubiao(self,driver):
        u"浮标检查"
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_02.1920x1080.png",way_name='channel')
        driver(className='android.widget.RelativeLayout',index=0).child(className="android.widget.TextView",index=0).click()
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_03.1920x1080.png",way_name='channel')
        driver(className='android.widget.RelativeLayout',index=0).child(className="android.widget.TextView",index=0).click()
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        driver(className='android.widget.RelativeLayout',index=0).child(className="android.widget.TextView",index=0).click()
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_05.1920x1080.png",way_name='channel')
        driver(className='android.widget.RelativeLayout',index=0).child(className="android.widget.TextView",index=0).click()
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_06.1920x1080.png",way_name='channel')
        driver(className='android.widget.RelativeLayout',index=0).child(className="android.widget.TextView",index=0).click()
        if self.wait_gone_images(driver, 'fubiao_06.1920x1080.png',way_name='channel'):
            log.info('浮标检查成功')
            return "OK"
        else:
            log.info('浮标检查失败')
            return None
        
    def ali(self,driver):
        u'''支付宝支付'''
        driver(className='android.widget.Button',index=0).click() #立即支付
        driver(className='android.widget.ListView',index=3).child(className="android.widget.RelativeLayout",index=1).click()
        self.click_images(driver,"ali_pay_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_pay_back_yes.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_02.1920x1080.png',way_name='channel'):
            log.info('支付宝支付成功')
            return "OK"
        else:
            log.info('支付宝支付失败')
            return None
        
    def wechat(self,driver):
        u'''微信支付'''
        sleep(1)
        driver(className='android.widget.ListView',index=3).child(className="android.widget.RelativeLayout",index=0).click() #微信支付
        sleep(3)
        driver(className='android.widget.LinearLayout',index=0).child(className="android.widget.ImageView",index=0).click() #退出微信
        driver(className='android.widget.Button',index=0).click() #微信退出确定
        driver(className='android.widget.ImageButton',index=0).click() #支付退出
        sleep(2)
        driver.press.back()
        driver(className='android.widget.Button',index=2).click() #支付退出
       
        if self.wait_gone_images(driver, 'exists_02.1920x1080.png',way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None
        
    def exitGame(self,driver):
        sleep(2)
        driver(className='android.widget.TextView',index=1).click()
        if self.wait_gone_images(driver, 'exists_02.1920x1080.png',way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None
    
