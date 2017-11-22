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
            driver.click(900,450)  # 点击输入框
            sleep(1)
            driver.clear_text()
            sleep(1)
            driver.type("17713623912",next=True)
            sleep(1)
            driver.type("test123")
            sleep(1)
            driver.click(900,785)  # 登录按钮
            sleep(2)
            driver.click(1330,110)  # 关闭弹框
            log.info('输入账号和密码登录')
            # self.click_images(driver,"idInput.1920x1080.png",way_name='channel')
            # sleep(1)
            # driver.type("17713623912")
            # self.click_images(driver,"pswInput.1920x1080.png",way_name='channel')
            # sleep(1)
            # driver.type("test123")
            # self.click_images(driver,u"login.1920x1080.png",way_name='channel')
            # self.click_images(driver,u"login_shiming_returnGame.1920x1080.png",way_name='channel')
        else:
            sleep(2)
            driver.click(1330,110)  # 关闭弹框
            log.info('自动登录')
        if self.wait_gone_images(driver, 'login_01.1920x1080.png',way_name="channel"):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None

    def fubiao(self,driver):
        driver.swipe(15,410,15,720,50)  # 移动浮标
        log.info('移动浮标')
        # self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_02.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_03.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_05.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_06.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'fubiao_05.1920x1080.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            log.info('浮标检查失败')
            return None 

    def ali(self,driver):
        u"支付宝支付"
        self.click_images(driver,"dangle_pay.1920x1080.png",way_name='channel')
        sleep(2)
        self.click_images(driver,"ali_pay_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_pay_back_yes.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_02.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None 
            
    def wechat(self,driver):
        u"微信支付"
        self.click_images(driver,"change_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat.1920x1080.png",way_name='channel')
        self.click_images(driver,"dangle_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"dangle_pay_close.1920x1080.png",way_name='channel')
        self.click_images(driver,"dangle_pay_close_yes.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None 
            
    def unionPay(self,driver):
        u"银联支付"
        self.click_images(driver,"change_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"unionPay.1920x1080.png",way_name='channel')
        self.click_images(driver,"dangle_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"unionPay_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"unionPay_back_yes.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png'):
            return 'ok'
        else:
            return None 
        
    def exitGame(self,driver):
        # self.click_images(driver,"setting.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_01.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_02.1920x1080.png",way_name='channel')
        driver.click(650,890)  # 残忍退出
        if self.wait_gone_images(driver, 'exitGame_02.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None
