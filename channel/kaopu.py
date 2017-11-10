#!/usr/bin/env python
# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'login_01.1920x1080.png',way_name='channel'):
            driver.click(950,420)  # 账号
            sleep(1)
            driver.clear_text()
            sleep(1)
            driver.type("13488958799",next=True)
            sleep(1)
            driver.type("luo118413")
            sleep(1)
            driver.click(900,700)  # 登录
            sleep(2)

            # self.click_images(driver,"idInput.1920x1080.png",way_name='channel')
            # sleep(1)
            # driver.type("15198139230")
            # self.click_images(driver,"pswInput.1920x1080.png",way_name='channel')
            # sleep(1)
            # driver.type("a123123")
            # self.click_images(driver,"login.1920x1080.png",way_name='channel')
            # self.click_images(driver,"login_shiming_returnGame.1920x1080.png",way_name='channel')
        else:
            # self.click_images(driver,"login_shiming_returnGame.1920x1080.png",way_name='channel')
            log.info('自动登录成功')
        if self.wait_gone_images(driver, 'login_01.1920x1080.png',way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None

    def exitGame(self,driver):
        sleep(1)
        driver.click(659,731)  # 退出游戏
        if self.wait_gone_images(driver, 'login_01.1920x1080.png',way_name='channel'):
            log.info('退出成功')
            return 'ok'
        else:
            log.info('退出失败')
            return None