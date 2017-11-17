# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'login_01.1920x1080.png',way_name='channel'):
            sleep(1)
            driver.click(900,920)  # 使用其他账号登录
            sleep(2)
            driver.click(550,610)  # 账号输入框
            sleep(1)
            driver.clear_text()
            driver.type("17713623912")
            sleep(1)
            driver.click(955,815)  # 关闭联想框
            sleep(1)
            driver.click(500,780)  # 密码输入框
            sleep(1)
            driver.type("test123")
            sleep(1)
            driver.click(530,1060)  # 登录
            log.info('输入账号密码登录')
        else:
            log.info('自动登录')
        if self.wait_gone_images(driver, 'login_01.1920x1080.png',way_name='channel'):
            log.info('浮标检查成功')
            return "OK"
        else:
            log.info('浮标检查失败')
            return None
        # if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
        #     driver(index=0, resourceId="com.oppo.usercenter:id/multi_autocomple_text").click()
        #     driver.clear_text()
        #     driver.type("17713623912")
        #     driver(index=0, resourceId="com.oppo.usercenter:id/edit_input_content").click()
        #     driver.clear_text()
        #     driver.type("test123")
        #     driver(index=4, resourceId="com.oppo.usercenter:id/btn_login").click()
        #     driver(index=0, resourceId="com.nearme.game.service:id/btn_nav").click()
        #     image = self.wait_gone_images(driver, 'exists_01.1920x1080.png',timeout=40,way_name='channel')
        #     if image:
        #         log.info('登录成功')
        #         return 'ok'
        #     else:
        #         log.info('登录失败')
        #         return None
        # else:
        #     driver(index=0, resourceId="com.nearme.game.service:id/btn_nav").click()
        #     image = self.wait_gone_images(driver, 'exists_01.1920x1080.png',way_name='channel')
        #     if image:
        #         log.info('自动登录成功')
        #         return 'ok'

    def fanhui(self,driver):
        sleep(3)
        driver(resourceId='com.nearme.atlas:id/btn_back',index=0).click()
        self.click_images(driver,"exit_pay_yes.1920x1080.png",way_name='channel')
        # driver(resourceId='com.nearme.atlas:id/dialog_standard_bt_yes',index=1).click()
        if self.wait_gone_images(driver, 'exists_02.1920x1080.png',way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None
        
    
    def fubiao(self,driver):
        u"浮标检查"
        log.info('暂时不处理浮标')
        # sleep(2)
        # driver.click(18,174)
        # driver.click(18,174)
        # driver(className="android.widget.RelativeLayout").child(text=u"福利").click()
        # driver(index=0, resourceId="com.nearme.game.service:id/back").click()
        # driver(className="android.widget.RelativeLayout").child(text=u"积分商城").click()
        # driver(index=0, resourceId="com.nearme.gamecenter:id/color_home_view").click()
        # driver(className="android.widget.RelativeLayout").child(text=u"可币券").click()
        # driver(index=0, resourceId="com.nearme.game.service:id/back").click()
        # driver(className="android.widget.RelativeLayout").child(text=u"论坛").click()
        # sleep(3)
        # driver.press.back()
        # driver(className="android.widget.RelativeLayout").child(text=u"消息").click()
        # driver(index=0, resourceId="com.nearme.game.service:id/back").click()
        # driver(className="android.widget.RelativeLayout").child(text=u"客服").click()
        # driver(index=0, resourceId="com.nearme.game.service:id/back").click()
        # driver(index=2, resourceId="com.nearme.game.service:id/close").click()
        # sleep(2)
        # driver.swipe(18,174,961,872)
        if self.wait_gone_images(driver, 'fubiao_01.1920x1080.png',way_name='channel'):
            log.info('浮标检查成功')
            return "OK"
        else:
            log.info('浮标检查失败')
            return None
        
    def ali(self,driver):
        u'''支付宝支付'''
        driver(className='android.widget.ListView',index=6).child(className='android.widget.LinearLayout',index=0).click() #支付宝支付
        driver(className='android.widget.LinearLayout',index=1).child(className='android.widget.Button',index=0).click()
        sleep(10)
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
        driver(className="android.widget.LinearLayout").child(text=u"微信支付").click()  #微信支付
        driver(className='android.widget.LinearLayout',index=1).child(className='android.widget.Button',index=0).click()
        sleep(5)
        driver(className='android.widget.LinearLayout',index=0).child(className="android.widget.ImageView",index=0).click() #退出微信
        driver(resourceId='com.nearme.atlas:id/btn_back',index=0).click()
        self.click_images(driver,"exit_pay_yes.1920x1080.png",way_name='channel')
        #sleep(2)
        #driver(resourceId='com.nearme.atlas:id/dialog_standard_bt_yes',index=1).click()
        if self.wait_gone_images(driver, 'exists_02.1920x1080.png',way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None
        
    def exitGame(self,driver):
        sleep(2)
        driver(resourceIdclassName='com.nearme.game.service:id/exit_btn',index=1).click()
        sleep(2)
        if self.wait_gone_images(driver, 'exists_02.1920x1080.png',way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None
