# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        driver(className='android.widget.Button',index=0,resourceId="android:id/button2").click()
        if self.images_or_none(driver, 'exists_02.1920x1080.png',way_name='channel'):
            driver(className='android.widget.LinearLayout',index=0).child(className="android.widget.EditText",index=0).click()
            driver.clear_text()
            driver.type("15883980943")
            driver(className='android.widget.LinearLayout',index=1).child(className="android.widget.EditText",index=0).click()
            driver.clear_text()
            driver.type("123456")
            driver(className='android.widget.Button',index=1).click()
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
        driver(className="android.widget.RelativeLayout", resourceId="com.huawei.gamebox:id/player_nickname").click()
        sleep(2)
        driver.press.back()
        driver(index=0, resourceId="com.huawei.gamebox:id/mine_score_linearlayout").click()
        driver(className="android.widget.ImageView", resourceId="com.huawei.gamebox:id/back_to_homepage").click()
        driver(index=1, resourceId="com.huawei.gamebox:id/mine_score_linearlayout").click()
        sleep(2)
        driver.press.back()
        driver(index=2, resourceId="com.huawei.gamebox:id/mine_score_linearlayout").click()
        sleep(2)
        driver.press.back()
        driver(index=3, resourceId="com.huawei.gamebox:id/mine_score_linearlayout").click()
        sleep(2)
        driver.press.back()
        sleep(2)
        driver.press.back()
        driver.press.back()
        if self.wait_gone_images(driver, 'fubiao_02.1920x1080.png',way_name='channel'):
            log.info('浮标检查成功')
            return "OK"
        else:
            log.info('浮标检查失败')
            return None
        
        
            
    def ali(self,driver):
        u'''支付宝支付'''
        '''
        sleep(2)
        #driver(className='android.widget.ListView',index=1).child(className="android.widget.LinearLayout",index=1).click()  #支付宝支付
        driver(className="android.widget.Button",index=3).click()
        sleep(8)
        driver(className='android.view.View',index=0).child(className="android.view.View",index=1).click() #支付宝返回
        driver(className='android.view.View',index=0).child(className="android.view.View",index=11).click() #支付宝确认返回
        '''
        self.click_images(driver,"ali_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_02.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_03.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_04.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'ali_01.1920x1080.png',way_name='channel'):
            log.info('支付宝支付成功')
            return "OK"
        else:
            log.info('支付宝支付失败')
            return None
        
    def wechat(self,driver):
        u'''微信支付'''
        '''
        driver(className='android.widget.ListView',index=1).child(className="android.widget.LinearLayout",index=2).click() #微信支付
        driver(className='android.widget.Button',index=3).click()
        sleep(3)
        driver(className='android.widget.RelativeLayout',index=0).child(className="android.widget.ImageView",index=0).click() #退出微信
        sleep(2)
        driver.keyevent('BACK')
        driver(className='android.widget.LinearLayout',index=1).child(className="android.widget.Button",index=1).click() #支付退出确定
        '''
        self.click_images(driver,"wechat_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_02.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_02.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_03.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_04.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'exists_02.1920x1080.png',way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None
        
    
        
        
        
                
        
        
        
        
        
                
        
        
