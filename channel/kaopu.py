#!/usr/bin/env python
# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'login.1920x1080.png',way_name='channel'):
        #self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,u"idInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("15198139230") 
            self.click_images(driver,u"pswInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("a123123")
            self.click_images(driver,u"login.1920x1080.png",way_name='channel')
            self.click_images(driver,u"login_shiming_returnGame.1920x1080.png",way_name='channel')
            if self.wait_gone_images(driver, 'login_shiming_returnGame.1920x1080.png',way_name='channel'):
                log.info('登录成功')
                return 'ok'
            else:
                log.info('登录失败')
                return None

        else:
            self.click_images(driver,u"login_shiming_returnGame.1920x1080.png",way_name='channel')
            if self.wait_gone_images(driver, 'login_shiming_returnGame.1920x1080.png',way_name='channel'):
                log.info('自动登录成功')
                return 'ok'
            
    def update(self,driver):
        self.click_images(driver,"update_01.1920x1080.png",way_name='channel')
        sleep(3)
        driver.click(750,800)