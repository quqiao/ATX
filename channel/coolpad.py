# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)
import configure


class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            driver(className='android.widget.LinearLayout',index=0).child(className="android.widget.MultiAutoCompleteTextView",index=1).click()
            driver.clear_text()
            driver.type("autotest1122")
            driver(className='android.widget.LinearLayout',index=1).child(className="android.widget.EditText",index=1).click()
            driver.clear_text()
            driver.type("123123")
            sleep(2)
            driver(className='android.widget.Button',index=2).click()
            sleep(2)
            driver(text=u'以后再说', className='android.widget.Button').click()

        else:
            # driver(text=u'以后再说', className='android.widget.Button').click()
            sleep(5)
            log.info('自动登录成功')
            return 'ok'

        if self.wait_gone_images(driver, 'exists_01.1920x1080.png',timeout=40,way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None
            
    def ali(self,driver):
        u'''支付宝支付'''
        driver(className='android.widget.LinearLayout',index=0).child(className="android.widget.ImageView",index=2).click() #支付宝支付
        if self.images_or_none(driver, 'ali_01.1920x1080.png',way_name='channel'):
            self.click_images(driver,"ali_01.1920x1080.png",way_name='channel')
            self.click_images(driver,"ali_02.1920x1080.png",way_name='channel')
        else:
            sleep(2)
            driver.keyevent('BACK')
        if self.images_or_none(driver, 'exists_02.1920x1080.png',way_name='channel'):
            log.info('支付宝支付成功')
            return "OK"
        else:
            log.info('支付宝支付失败')
            return None
        
    def wechat(self,driver):
        u'''微信支付'''
        driver(className='android.widget.LinearLayout',index=2).child(className="android.widget.ImageView",index=2).click() #微信支付
        driver(className='android.widget.LinearLayout',resourceId="com.tencent.mm:id/h6").click() #微信支付返回
        driver(className='android.widget.RelativeLayout',resourceId="com.crisisfire.android.kp:id/back_re").click() #退出充值界面
        driver(className='android.widget.LinearLayout',index=4).child(className="android.widget.TextView",index=2).click() #退出充值界面确定
        
        if self.wait_gone_images(driver, 'exists_02.1920x1080.png',way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None
    
    def restart(self,driver):
        sleep(1)
        driver.press.home()
        sleep(1)
        driver.start_app(configure.package_name,configure.activity_name)
        if self.wait_gone_images(driver, 'exists_02.1920x1080.png',way_name='channel'):
            log.info('重启成功')
            return "OK"
        else:
            log.info('重启失败')
            return None
        
    def exitGame(self,driver):
        print '没有内容'
        if self.wait_gone_images(driver, 'exists_02.1920x1080.png',way_name='channel'):
            log.info('重启成功')
            return "OK"
        else:
            log.info('重启失败')
            return None
        
    