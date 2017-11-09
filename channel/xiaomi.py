# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'exists_02.1920x1080.png',way_name='channel',timeout=10):
            self.click_images(driver,"shiming_close.1920x1080.png",way_name='channel')
            sleep(2)
            driver(className='android.widget.RelativeLayout',index=1).child(className="android.widget.TextView",index=2).click()
            image = self.wait_gone_images(driver, 'exists_01.1920x1080.png',timeout=40,way_name='channel')
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
        sleep(8)
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_02.1920x1080.png",way_name='channel')
        driver(className='android.widget.GridView',index=0).child(className="android.widget.LinearLayout",index=0).click()
        driver(index=0, resourceId="com.xiaomi.gamecenter.sdk.service:id/back").click()
        driver(className='android.widget.GridView',index=0).child(className="android.widget.LinearLayout",index=1).click()
        driver(index=0, resourceId="com.xiaomi.gamecenter.sdk.service:id/back").click()
        driver(className='android.widget.GridView',index=0).child(className="android.widget.LinearLayout",index=2).click()
        driver(index=0, resourceId="com.xiaomi.gamecenter.sdk.service:id/back").click()
        driver(className="android.widget.RelativeLayout").child(text=u"隐藏").click()
        if self.wait_gone_images(driver, 'fubiao_02.1920x1080.png',way_name='channel'):
            log.info('浮标检查成功')
            return "OK"
        else:
            log.info('浮标检查失败')
            return None
    
    
    def ali(self,driver):
        u'''支付宝支付'''
        self.click_images(driver,"ali.1920x1080.png",way_name='channel')
        self.click_images(driver,"xiaomi_pay.1920x1080.png",way_name='channel')
        sleep(3)
        driver.press.back()
        sleep(3)
        driver.press.back()
        if self.wait_gone_images(driver, 'exists_02.1920x1080.png',way_name='channel'):
            log.info('支付宝支付成功')
            return "OK"
        else:
            log.info('支付宝支付失败')
            return None
        
    def wechat(self,driver):
        u'''微信支付'''
        self.click_images(driver,"wechat.1920x1080.png",way_name='channel')   #选择微信
        self.click_images(driver,"xiaomi_pay.1920x1080.png",way_name='channel')
        driver(className='android.widget.LinearLayout',index=0).child(className="android.widget.ImageView",index=0).click() #退出充值界面
        if self.wait_gone_images(driver, 'exists_02.1920x1080.png',way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None
        
        
    def Exitgame(self,driver):
        self.click_images(driver,"Exitgame_01.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'Exitgame_01.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return "OK"
        else:
            log.info('退出游戏失败')
            return None