# coding=utf-8


from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        self.click_images(driver,"QQlogin.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exist_login_01.1920x1080.png',way_name='channel'):
            self.click_images(driver,"yingyongbao_exist_login.1920x1080.png",way_name='channel')
        elif self.images_or_none(driver, 'idInput.1920x1080.png',way_name='channel'):
            self.click_images(driver,"idInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("Ewan10000") 
            self.click_images(driver,"pswInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("123456")
            self.click_images(driver,"login.1920x1080.png",way_name='channel')
        else:
            log.info('自动登录成功')
        if self.wait_gone_images(driver,"yingyongbao_exist_login.1920x1080.png",way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None

    def QQ(self,driver):
        u"QQ钱包支付"
        self.click_images(driver,"yingyongbao_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"QQ.1920x1080.png",way_name='channel')
        sleep(3)
        driver.keyevent("BACK")
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def wechat(self,driver):
        u"微信支付"
        # self.click_images(driver,"yingyongbao_changge_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat.1920x1080.png",way_name='channel')
        # self.click_images(driver,"yingyongbao_pay_yes.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_back.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None