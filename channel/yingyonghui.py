# coding=utf-8


from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'login_01.1920x1080.png',way_name='channel'):
            driver.click(800,1200)  # 切换账号登录
            sleep(2)
            driver.click(350,580)  # 用户名输入
            sleep(1)
            driver.type("15198139230",next=True)
            sleep(1)
            driver.type("a123123")
            sleep(1)
            driver.click(520,950)  #登录
            log.info('输入账号密码登录')
            # self.click_images(driver,"idInput.1920x1080.png",way_name='channel')
            # sleep(1)
            # driver.type("15198139230")
            # self.click_images(driver,"pswInput.1920x1080.png",way_name='channel')
            # sleep(1)
            # driver.type("a123123")
            # self.click_images(driver,"login.1920x1080.png",way_name='channel')
        else:
            log.info('自动登录')
        if self.wait_gone_images(driver,"login_01.1920x1080.png",way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None
              

    def ali(self,driver):
        u"支付宝支付"
        self.click_images(driver,"pay_shiming_close.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_pay_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_pay_back_yes.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def wechat(self,driver):
        u"微信支付"
        self.click_images(driver,"wechat.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_back.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def yingyongdou(self,driver):
        u"应用豆支付"
        if self.get_view_info(driver) == channel_pay_activity:
            self.click_images(driver,"yingyongdou.1920x1080.png",way_name='channel')
            self.click_images(driver,"yingyongdou_pay_cancel.1920x1080.png",way_name='channel')
            
    def caifutong(self,driver):
        u"财付通支付"
        if self.get_view_info(driver) == channel_pay_activity:
            self.click_images(driver,"caifutong.1920x1080.png",way_name='channel')
            self.click_images(driver,"yingyongdou_pay_back.1920x1080.png",way_name='channel')
            self.click_images(driver,"yingyongdou_pay_back_yes.1920x1080.png",way_name='channel')
            
    def phonePay(self,driver):
        u"手机支付"
        if self.get_view_info(driver) == channel_pay_activity:
            self.click_images(driver,"phonePay.1920x1080.png",way_name='channel')
            self.click_images(driver,"phonePay_back.1920x1080.png",way_name='channel')

    def exitGame(self,driver):
        log.info('应用汇没有渠道退出')
        if self.wait_gone_images(driver,"login_01.1920x1080.png",way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            log.info('退出游戏失败')
            return None

    def fubiao(self,driver):
        driver.click(10,869)  # 隐藏浮标
        sleep(1)
        driver.click(60,900)  # 浮标
        sleep(2)
        driver.click(535,450)  # 礼包
        sleep(2)
        driver.click(868,450)  # 消息
        sleep(2)
        driver.click(950,130)  # 关闭
        sleep(2)
        if self.wait_gone_images(driver,"fubiao_01.1920x1080.png",way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            log.info('退出游戏失败')
            return None





            



