# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'exists_01.1280x720.png',way_name='channel'):
            driver(className='android.widget.LinearLayout',index=0).child(className="android.widget.EditText",index=0).click()
            driver.clear_text()
            driver.type("15883980943")
            driver(className='android.widget.LinearLayout',index=1).child(className="android.widget.EditText",index=0).click()
            driver.clear_text()
            driver.type("123456")
            driver(className='android.widget.Button',index=1).click()
            image = self.wait_gone_images(driver, 'exists_01.1280x720.png',timeout=40,way_name='channel')
            if image:
                log.info('登录成功')
                return 'ok'
            else:
                log.info('登录失败')
                return None
        else:
            image = self.wait_gone_images(driver, 'exists_01.1280x720.png',way_name='channel')
            if image:
                log.info('自动登录成功')
                return 'ok'
            
    def ali(self,driver):
        u'''支付宝支付'''
        driver(className='android.widget.RelativeLayout',index=3).child(className="android.widget.ImageView",index=2).click() #支付宝支付
        driver(className='android.view.View',index=0).child(className="android.view.View",index=1).click() #支付宝返回
        driver(className='android.webkit.WebView',index=0).child(className="android.view.View",index=6).click() #支付宝确认返回
        if self.images_or_none(driver, 'exists_02.1280x720.png',way_name='channel'):
            log.info('支付宝支付成功')
            return "OK"
        else:
            log.info('支付宝支付失败')
            return None
        
    def wechat(self,driver):
        u'''微信支付'''
        driver(className='android.widget.RelativeLayout',index=4).child(className="android.widget.ImageView",index=2).click() #微信支付
        driver(className='android.widget.LinearLayout',resourceId="com.tencent.mm:id/hf").click()
        driver(className='android.widget.RelativeLayout',index=0).child(className="android.widget.ImageView",index=0).click() #退出充值界面
        if self.wait_gone_images(driver, 'exists_02.1280x720.png',way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None
        
        
        
        
                
        
        