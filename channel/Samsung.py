# coding=utf-8


from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'pswInput.1920x1080.png',way_name='channel',timeout=10):
                driver.press.back()
                # self.click_exists(driver, 'cancel_auto_login.1920x1080.png',way_name='channel')
                self.click_images(driver,"idInput.1920x1080.png",way_name='channel')
                sleep(1)
                driver.type("hero002",next=True)
                sleep(1)
                driver.type("111111")
                self.click_images(driver,"login.1920x1080.png",way_name='channel')
                self.click_images(driver,"bangding.1920x1080.png",way_name='channel')
                log.info('输入帐号密码登录')
        else:
            self.click_images(driver,"bangding.1920x1080.png",way_name='channel')
            log.info('自动登录成功')
        if self.wait_gone_images(driver, 'login.1920x1080.png',way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None

    def fubiao(self,driver):
        log.info('暂时不操作浮标')
        # self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_02.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_03.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_05.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_06.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_07.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_08.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_09.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        # self.click_images(driver,"fubiao_10.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'login.1920x1080.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None 
        
    def ali(self,driver):
        u"支付宝支付"
        #if self.get_view_info(driver) == channel_pay_activity:
        self.click_images(driver,"ali.1920x1080.png",way_name='channel')
        sleep(10)
        driver.press.back()
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None 
            
    def wechat(self,driver):
        u"微信支付"
        #if self.get_view_info(driver) == channel_pay_activity:
        self.click_images(driver,"wechat.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"pay_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"pay_back_yes.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'pay_back_yes.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None 
            
    def phonePay(self,driver):
        u"手机点卡支付"
        #if self.get_view_info(driver) == channel_pay_activity:
        self.click_images(driver,"anzhi_pay_changepay.1920x1080.png",way_name='channel')
        self.click_images(driver,"phonePay.1920x1080.png",way_name='channel')
        self.click_images(driver,"anzhi_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"phonePay_back.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_04.1920x1080.png'):
            return 'ok'
        else:
            return None
        
    def exitGame(self,driver):
        # self.click_images(driver,"setting.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_01.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_02.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_03.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_04.1920x1080.png",way_name='channel')
        sleep(2)
        driver.click(1150,700)  # 原生的退出
        if self.wait_gone_images(driver, 'exitGame_04.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None
        
    def lingzuan(self,driver):
        self.click_images(driver,"lingzuan_01.1920x1080.png",way_name='channel')
        sleep(2)
        driver(className="android.view.View",description='每日成功分享（0/1）').click()
        self.click_images(driver,"lingzuan_02.1920x1080.png",way_name='channel')
        self.click_images(driver,"lingzuan_03.1920x1080.png",way_name='channel')
        sleep(2)
        driver(className="android.view.View",description='每日成功分享（0/1）').click()
        self.click_images(driver,"lingzuan_04.1920x1080.png",way_name='channel')
        self.click_images(driver,"lingzuan_03.1920x1080.png",way_name='channel')
        sleep(4)
        driver(className="android.view.View",description='每日成功分享（0/1）').click()
        self.click_images(driver,"lingzuan_05.1920x1080.png",way_name='channel')
        sleep(5)
        driver.press.back()
        sleep(2)
        driver(className="android.view.View",description='每日成功分享（0/1）').click()
        self.click_images(driver,"lingzuan_06.1920x1080.png",way_name='channel')
        sleep(5)
        driver.press.back()
        sleep(2)
        driver(className="android.view.View",description='每日成功分享（0/1）').click()
        self.click_images(driver,"lingzuan_07.1920x1080.png",way_name='channel') 
        sleep(5)
        driver.press.back()
        driver.press.back()
        sleep(1)
        driver(className="android.widget.TextView",text="不保存").click()
        self.click_images(driver,"lingzuan_08.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'lingzuan_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
        
        
        
        
            
    

        
        
        
        
            
    

