#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
packages_name   activity_name  可以在终端 输入 python -m atx apkparse <package_path> 

'''
'''
a = raw_input("package_name:")
print a
b = raw_input("activity_name:")
print b
'''

device_name = ''
game_name = 'sjsgz'
channel_name = 'baidu'
package_name = 'com.sjsgz.hero'
activity_name = 'mobi.xy3d.tstd.SplashActivity'

#quick
'''
#channel_name = 'quick'
#package_name = 'com.crisisfire.cmgeQ' #全民枪战
#activity_name = 'com.crisisfire.cmgeQ.SplashActivity'    #全民枪战
#package_name = 'com.fengniao.games.HZ.aSkymoon'   #巅峰战舰
#activity_name = 'com.games.HZ.SDK.SplashActivity'    #巅峰战舰
#package_name = 'com.tqyouxi.xlj2.local'   #三生问道
#activity_name = 'com.tqyouxi.sdk.SplashActivity'    #三生问道
#package_name = 'com.wyd.ddfc.quick'   #一起来飞车
#activity_name = 'com.wyd.fc.activity.SplashActivity'    #一起来飞车
#package_name = 'com.taiyouxi.ifsg.quick'   #极无双
#activity_name = 'com.taiyouxi.a3k.SplashActivity'    #极无双
#package_name = 'com.yingxiong.jiujian.Android'   #九剑魔龙传
#activity_name = 'com.YouYiFang.NewGame.SplashActivity'    #九剑魔龙传
#package_name = 'com.fengniao.games.QTDL.aSkymoon'   #抢滩登陆
#activity_name = 'com.fengniao.games.QTDL.SDK.SplashActivity'    #抢滩登陆
#package_name = 'com.qihoo.wm'   #一起来跳舞
#activity_name = 'com.ttxw.quicker.SplashActivity'    #一起来跳舞
#package_name = 'm.Sgame.yzr2.quick'   #影之刃
#activity_name = 'm.Sgame.yzr2.SplashActivity'    #影之刃
#package_name = 'com.wyd.hero.dandandao'   #弹弹岛
#activity_name = 'com.excelliance.open.KXQP'    #弹弹岛
#package_name = 'com.ea.android.chs.nbamobile'   #NBA
#activity_name = 'com.ea.game.nba.QkSplashActivity'    #NBA
#package_name = 'mobi.xy3d.tstd'   #生煎三国志
#activity_name = 'mobi.xy3d.tstd.SplashActivity'    #生煎三国志
'''

# 游戏名
'''
game_name_01 = 'ddd'  # 弹弹岛
game_name_02 = 'dfzj'  # 巅峰战舰
game_name_03 = 'jjmlz'  # 九剑魔龙传
game_name_04 = 'jws'   # 极无双
game_name_05 = 'NBA'   # NBA
game_name_06 = 'qmqz2'  # 全名枪战
game_name_07 = 'qtdl3D' # 抢滩登陆3D
game_name_08 = 'sswd'  # 三生问道
game_name_09 = 'yqlfc'  # 一起来飞车
game_name_10 = 'yqltw'  # 一起来跳舞
game_name_11 = 'yzr'  # 影之刃2
game_name_12 = 'sjsgz'  # 生煎三国志
'''

#渠道名
'''
channel_name_01 = '360' # 360
channel_name_02 = '37wan' # 37玩
channel_name_03 = '4399'  # 4399
channel_name_04 = 'anzhi'  # 安智
channel_name_05 = 'baidu'  # 百度
channel_name_06 = 'chushou'  # 触手
channel_name_07 = 'coolpad'  # 酷派
channel_name_08 = 'dangle'  # 当乐
channel_name_09 = 'ewan'  # 益玩
channel_name_10 = 'Gionee'  # 金立
channel_name_11 = 'guanfang'  # 官方
channel_name_12 = 'guopan'  # 果盘
channel_name_13 = 'HTC'  # HTC
channel_name_14 = 'huawei'  # 华为
channel_name_15 = 'kugou'  # 酷狗
channel_name_16 = 'Lenovo'  # 联想
channel_name_17 = 'meizu'  # 魅族
channel_name_18 = 'muzhiwan'  # 拇指玩
channel_name_19 = 'oppo'  # OPPO
channel_name_20 = 'papa'  # 啪啪
channel_name_21 = 'PPS'  # 爱奇艺（PPS)
channel_name_22 = 'quick'  # 母包
channel_name_23 = 'Samsung'  # 三星
channel_name_24 = 'sina'  # 新浪
channel_name_25 = 'sougou'  # 搜狗
channel_name_26 = 'telecom'  # 电信
channel_name_27 = 'UC'  # UC
channel_name_28 = 'unicom'  # 联通
channel_name_29 = 'vivo'  # vivo
channel_name_30 = 'wandoujia'  # 豌豆荚
channel_name_31 = 'xiaomi'  # 小米
channel_name_32 = 'yingyongbao'  # 应用宝
channel_name_33 = 'yingyonghui'  # 应用汇
channel_name_34 = 'youku'  # 优酷
channel_name_35 = 'kaopu'  # 酷派
channel_name_36 = 'youketianxia'  # 游客天下
channel_name_37 = 'douyu'  # 斗鱼
channel_name_38 = 'huya'   # 虎牙（账号需要验证码）
channel_name_39 = 'leshi'  # 乐视
channel_name_40 = 'pptv'  # PPTV
channel_name_41 = 'jinritoutiao'  # 今日头条
channel_name_42 = 'kuaikan'  # 快看
'''
  
#极无双
'''
activity_name = 'com.taiyouxi.a3k.SplashActivity'
package_name = 'com.taiyouxi.jiwushuang.vivo'
package_name = 'com.taiyouxi.jiwushuang.samsung'
package_name = 'com.taiyouxi.jiwushuang.yyh'
package_name = 'com.taiyouxi.qihoo360'
package_name = 'com.taiyouxi.jiwushuang.lenovo'
package_name = 'com.taiyouxi.jiwushuang.leshi'
package_name = 'com.taiyouxi.jiwushuang.coolpad'
package_name = 'com.taiyouxi.ifsanguo.huawei'
package_name = 'com.taiyouxi.jiwushuang.downjoy'
package_name = 'com.taiyouxi.jiwushuang.egame'
package_name = 'com.taiyouxi.ifsanguo.m4399'
package_name = 'com.taiyouxi.jiwushuang.papa'
package_name = 'com.taiyouxi.jiwushuang.am'
package_name = 'com.taiyouxi.jiwushuang.mzw'
package_name = 'com.taiyouxi.jiwushuang.migu'
package_name = 'com.taiyouxi.jiwushuang.mz'
package_name = 'com.taiyouxi.jiwushuang.yanmeng.ymplay'
package_name = 'com.taiyouxi.jiwushuang.oppo.nearme.gamecenter'
package_name = 'com.tencent.tmgp.ifsanguo'
package_name = 'com.taiyouxi.jiwushuang.pptv'
package_name = 'com.taiyouxi.jiwushuang.wogame'
package_name = 'com.taiyouxi.jiwushuang.iqiyi'
package_name = 'com.taiyouxi.jiwushuang.wdj'
package_name = 'com.taiyouxi.jiwushuang.sogou.com'
package_name = 'com.taiyouxi.jiwushuang.kaopu'
package_name = 'com.taiyouxi.jiwushuang.anzhi'
package_name = 'com.taiyouxi.ifsanguo.baidu'
package_name = 'com.taiyouxi.ifsanguo.mi'
package_name = 'com.taiyouxi.ifsanguo.uc'
package_name = 'com.taiyouxi.jiwushuang.jrwan'
package_name = 'com.taiyouxi.jiwushuang.guopan'
package_name = 'com.taiyouxi.jiwushuang.tt'
'''

#影之刃
'''
activity_name = 'm.Sgame.yzr2.SplashActivity'
package_name = 'com.zy.yzr2.kaopu'
package_name = 'com.zy.yzr2.cstv'
'''

#一起来跳舞
'''
activity_name = 'com.ttxw.yktx.YKTXActivity'  #游客天下专用activity
activity_name = 'com.ttxw.quicker.SplashActivity'
package_name = 'com.ttxw.yktx'
'''

# 生煎三国志
'''
activity_name = 'mobi.xy3d.tstd.SplashActivity'
package_name = 'com.yx.sjsgz.sougou' # 搜狗
package_name = 'com.yx.sjsgz.iqiyi'  # 爱奇艺
package_name = 'com.yx.sjsgz.lenovo' # 联想
package_name = 'com.yx.sjsgz.coolpad'  # 酷派
package_name = 'com.sjs.mi'  # 小米
package_name = 'com.yx.tstd.baidu'  # 百度
package_name = 'com.yx.sjsgz.vivo'  # vivo
package_name = 'com.yx.sjsgz.nearme.gamecenter'  # OPPO
package_name = 'com.yx.sjsgz.qihoo360'  # 360
package_name = 'com.yx.sjsgz.anzhi'  # 安智
package_name = 'com.yx.sjsgz.m4399'  # 4399
package_name = 'com.yx.sjsgz.pptv'  # pptv
package_name = 'com.yx.sjsgz.douyu'  # 斗鱼
package_name = 'com.yx.sjsgz.huawei'  # 华为
package_name = 'com.yx.sjsgz.downjoy.wm'  # 当乐
package_name = 'com.yx.sjsgz.mz'  # 魅族
package_name = 'com.yx.sjsgz.guopan'  # 果盘
package_name = 'com.tencent.tmgp.com.sjsgz'  # 应用宝
package_name = 'com.yx.sjsgz.mzw'  # 拇指玩
package_name = 'com.yx.sjsgz.am'  # 金立
package_name = 'com.yx.sjsgz.yyh'  # 应用汇
package_name = 'mobi.xy3d.tstdgj.uc'  # UC
package_name = 'com.sjsgz.hero'  # 官方
'''

# 一起来飞车
"""
activity_name = 'com.wyd.fc.activity.SplashActivity'    # 一起来飞车
activity_name = 'com.wyd.passport.impl.FirstActivity'    # UC，乐视
package_name = 'com.wyd.hero.yqlfc.cb1.samsung'   # 三星
package_name = 'com.wyd.hero.yqlfc.cb1.baidu'   # 百度
package_name = 'com.wyd.hero.yqlfc.cb1.mcbg'   # 虎牙
package_name = 'com.wyd.hero.yqlfc.cb1.uc'   # UC
package_name = 'com.wyd.hero.yqlfc.cb1.leshi'   # 乐视手机
package_name = 'com.wyd.hero.yqlfc.cb1.nearme.gamecenter'   # OPPO
package_name = 'com.wyd.hero.yqlfc.cb1.pptv'   # pptv
package_name = 'com.wyd.hero.yqlfc.cb1.huawei'   # 华为
package_name = 'com.wyd.hero.yqlfc.cb1.egame'   # 电信爱游戏
package_name = 'com.wyd.hero.yqlfc.cb1.qihoo'   # 360
package_name = 'com.wyd.hero.yqlfc.cb1.mi'   # 小米
package_name = 'com.wyd.hero.yqlfc.cb1.iqiyi'   # 爱奇艺（pps)
package_name = 'com.wyd.hero.yqlfc.cb1.zy'   # 掌阅
package_name = 'com.wyd.hero.yqlfc.cb1.mz'   # 魅族
package_name = 'com.wyd.hero.yqlfc.cb1.kaopu'   # 靠谱
package_name = 'com.wyd.hero.yqlfc.cb1.vivo'   # vivo
package_name = 'com.wyd.hero.yqlfc.cb1.downjoy'   # 当乐
package_name = 'com.wyd.hero.yqlfc.cb1.kuaikan'   # 快看
package_name = 'com.wyd.hero.yqlfc.cb1.coolpad'   # 酷派
package_name = 'com.wyd.hero.yqlfc.cb1.lenovo'   # 联想
package_name = 'com.wyd.hero.yqlfc.cb1.am'   # 金立
package_name = 'com.wyd.hero.yqlfc.cb1.cstv'   # 触手
package_name = 'com.wyd.hero.yqlfc.cb1.ewan'   # 益玩
package_name = 'com.wyd.hero.yqlfc.cb1.jrtt'   # 今日头条
package_name = 'com.wyd.hero.yqlfc.cb1.m4399'   # 4399
package_name = 'com.wyd.hero.yqlfc.cb1.mzw'   # 拇指玩
package_name = 'com.wyd.hero.yqlfc.cb1.anzhi'   # 安智
package_name = 'com.wyd.hero.yqlfc.cb1.yyh'   # 应用汇
package_name = 'com.tencent.tmgp.yqlfc'   # 应用宝
package_name = 'com.wyd.hero.yqlfc.cb1.sogou.com'   # 搜狗
"""

# 全民枪战
"""
activity_name = 'com.unicom.dcLoader.welcomeview'    # 联通专用
package_name = 'com.crisisfire.android.wolt'   # 联通
"""

