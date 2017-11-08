#!/usr/bin/env python
# coding=utf-8



from time import sleep, strftime,time
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def login(self, driver):
        '''渠道login'''
        if self.images_or_none(driver, 'login_01.1920x1080.png',way_name='channel'):
            self.click_images(driver,"login_01.1920x1080.png",way_name='channel')
            self.click_images(driver,"login_02.1920x1080.png",way_name='channel')
            driver.type('18200130399',next=True)
            sleep(1)
            driver.type('5668080')
            sleep(2)
            driver.click(910,710)#进入游戏按钮
        else:
            print '自动登录'
        if self.wait_gone_images(driver, 'login_02.1920x1080.png',way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None