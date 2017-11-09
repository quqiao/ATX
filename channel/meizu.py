# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def login(self, driver):
        u"渠道login"
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            driver(className='android.widget.LinearLayout',index=1).child(className="android.widget.RelativeLayout",index=3).click()
            driver(className='android.widget.LinearLayout',index=0).child(className="android.widget.EditText",index=0).click()
            driver.clear_text()
            driver.type("markettest@flyme.cn")
            driver(className='android.widget.LinearLayout',index=1).child(className="android.widget.EditText",index=0).click()
            driver.clear_text()
            driver.type("ck123456")
            driver(className='android.widget.Button',index=0).click()
            if self.wait_gone_images(driver, 'exists_01.1920x1080.png',timeout=40,way_name='channel'):
                log.info('登录成功')
                return 'ok'
            else:
                log.info('登录失败')
                return None
        else:
            if self.wait_gone_images(driver, 'exists_01.1920x1080.png',way_name='channel'):
                log.info('自动登录成功')
                return 'ok'
    
    def ali(self,driver):
        u'''支付宝支付'''
        driver(className='android.widget.LinearLayout',index=3).child(className='android.widget.LinearLayout',index=0).click() #支付宝支付
        driver(className="android.widget.LinearLayout").child(text=u"支付宝").click()
        driver(className="android.widget.RelativeLayout").child(text=u"立即支付").click()
        sleep(5)
        driver.press.back()
        if self.images_or_none(driver, 'exists_02.1920x1080.png',way_name='channel'):
            log.info('支付宝支付成功')
            return "OK"
        else:
            log.info('支付宝支付失败')
            return None
        
    def wechat(self,driver):
        u'''微信支付'''
        sleep(1)
        driver(className='android.widget.LinearLayout',index=3).child(className='android.widget.LinearLayout',index=0).click()  #微信支付
        driver(className="android.widget.LinearLayout").child(text=u"微信支付").click()
        driver(className="android.widget.RelativeLayout").child(text=u"立即支付").click()
        driver(className='android.widget.LinearLayout',index=0).child(className='android.widget.ImageView',index=0).click()
        driver(resourceId="com.meizu.gamecenter.service:id/iv_close",index=1).click()
        if self.wait_gone_images(driver, 'exists_02.1920x1080.png',way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None
        
    def exitGame(self,driver):
        sleep(2)
        driver(className="android.widget.LinearLayout").child(text=u"离开游戏").click()
        if self.wait_gone_images(driver, 'exists_03.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return "OK"
        else:
            log.info('退出游戏失败')
            return None
    