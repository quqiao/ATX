# coding=utf-8


from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        self.click_images(driver,u"yingyonghui_change_login.1920x1080.png",way_name='channel')
        self.click_images(driver,u"idInput.1920x1080.png",way_name='channel')
        sleep(1)
        driver.type("15198139230") 
        self.click_images(driver,u"pswInput.1920x1080.png",way_name='channel')
        sleep(1)
        driver.type("a123123")
        self.click_images(driver,u"login.1920x1080.png",way_name='channel')
              

    def ali(self,driver):
        u"支付宝支付"
        if self.get_view_info(driver) == channel_pay_activity:
            self.click_images(driver,"ali.1920x1080.png",way_name='channel')
            self.click_images(driver,"ali_pay_back.1920x1080.png",way_name='channel')
            self.click_images(driver,"ali_pay_back_yes.1920x1080.png",way_name='channel')
            
    def wechat(self,driver):
        u"微信支付"
        if self.get_view_info(driver) == channel_pay_activity:
            self.click_images(driver,"wechat.1920x1080.png",way_name='channel')
            self.click_images(driver,"wechat_back.1920x1080.png",way_name='channel')
            
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
        u"财付通支付"
        if self.get_view_info(driver) == channel_pay_activity:
            self.click_images(driver,"phonePay.1920x1080.png",way_name='channel')
            self.click_images(driver,"phonePay_back.1920x1080.png",way_name='channel')

            




            




