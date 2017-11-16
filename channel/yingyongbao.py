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
            driver.click(750,530)  # QQ登录
            sleep(2)
            driver.click(530,1450)  # 登录
            sleep(1)
            log.info('QQ登录')
        else:
            log.info('自动登录成功')
        if self.wait_gone_images(driver,"yingyongbao_exist_login.1920x1080.png",way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None

    def fubiao(self,driver):
        log.info('不用')
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

    def exitGame(self,driver):
        log.info('该渠道没有退出游戏功能')
        if self.wait_gone_images(driver, 'login_01.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None