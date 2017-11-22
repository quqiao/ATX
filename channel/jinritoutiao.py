# coding=utf-8
#!/usr/bin/env python

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver,"login_01.1920x1080.png",way_name='channel'):
            sleep(1)
            driver.click(950,480)  # 点击账号
            sleep(1)
            driver.clear_text()
            sleep(1)
            driver.type("15114089697",next=True)
            sleep(1)
            driver.type("123456")
            sleep(1)
            driver.click(1160,750)  # 登录
            sleep(2)
            driver.click(600,239)  # 隐藏浮层
            log.info('输入账号登录')
        else:
            sleep(1)
            driver.click(600,239)  # 隐藏浮层
            sleep(2)
            log.info('自动登录')
        if self.wait_gone_images(driver, 'login_01.1920x1080.png',way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None

    def fubiao(self,driver):
        log.info('没有浮标')
        if self.wait_gone_images(driver, 'login_01.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None

    def exitGame(self,driver):
        log.info('该渠道没有退出框')
        if self.wait_gone_images(driver, 'login_01.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None