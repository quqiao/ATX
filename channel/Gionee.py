# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'exists_02.1920x1080.png',way_name='channel'):
            driver(index=0, resourceId="com.gionee.gsp:id/username_edittext").click()
            driver.clear_text()
            driver.type("15202828543")
            driver(index=0, resourceId="com.gionee.gsp:id/password_edittext").click()
            driver.clear_text()
            driver.type("123456")
            driver(className='android.widget.RelativeLayout',index=1).child(className='android.widget.Button',index=0).click()
            driver(className='android.widget.Button',index=0).click()
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
        driver(className='android.widget.RelativeLayout',resourceId="com.gionee.gsp:id/other_chan_rela_layout").click()
        driver(className='android.widget.RelativeLayout',index=1).click() #支付宝支付
        sleep(2)
        driver.press.back()
        #self.click_images(driver,"ali_pay_back.1920x1080.png",way_name='channel')
        #self.click_images(driver,"ali_pay_back_yes.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_02.1920x1080.png',way_name='channel'):
            log.info('支付宝支付成功')
            return "OK"
        else:
            log.info('支付宝支付失败')
            return None
        
    def wechat(self,driver):
        u'''微信支付'''
        sleep(1)
        driver(className='android.widget.ListView',index=2).child(className='android.widget.RelativeLayout',index=0).click() #微信支付
        sleep(3)
        driver(className='android.widget.LinearLayout',index=0).child(className="android.widget.ImageView",index=0).click() #退出微信
        driver(className='android.widget.RelativeLayout',index=0).child(className="android.widget.ImageView",index=0).click() #支付退出确定
       
        if self.wait_gone_images(driver, 'exists_02.1920x1080.png',way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None
        
    def exitGame(self,driver):
        #sleep(1)      
        #driver(className='android.widget.Button',index=1).click()
        self.click_images(driver,"exitGame_01.1920x1080.png",way_name='channel')
    
        
        
        
                
        
        
        
        
        
                
        
        

        
    
        
        
        
                
        
        
        
        
        
                
        
        
