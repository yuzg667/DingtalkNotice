# -*- coding: UTF-8 -*-
'''
pip install DingtalkChatbot
pip install sxtwl
'''

from dingtalkchatbot.chatbot import DingtalkChatbot
import time
import  sxtwl
lunar = sxtwl.Lunar()  
from One2TwoDigit import One2TwoDigit,addYear
from differ_days import date_part
import datetime

# 初始化机器人小丁
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=f6a1025b57719fbd2b1bf5d9b279d7b233bb59de20335890d46f60603d4817ce'  #小号
xiaoding = DingtalkChatbot(webhook)

ymc = ["11", "12", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10" ]
rmc = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]    
def birthdayNotice_job(bri_name,bri_mon,bri_day,futureDays=3):
    print("birthdayNotice_job is working...")
    dayYinli2Yangli = lunar.getDayByLunar(int(time.strftime("%Y")), bri_mon, bri_day , False)  #查询阴历2018年10月20日的信息，最后一个False表示是否是润月，填True的时候只有当年有润月的时候才生效
    yangliDay = (str(dayYinli2Yangli.y) + One2TwoDigit(str(dayYinli2Yangli.m)) + One2TwoDigit(str(dayYinli2Yangli.d)))
    yangliDayMsg ='农历:' + (str(bri_mon) + '月' + (str(bri_day)) + '日' )
    print(bri_name+'阳历生日是:'+yangliDay)
    d2 = date_part(yangliDay) 
    d1 = date_part(date=datetime.datetime.now().strftime('%Y%m%d'))
    differ_day = (d2 - d1).days
    
    if 0<differ_day<=futureDays:
        name = bri_name
        xiaoding.send_text(msg= yangliDayMsg + '是【' + name + '】的生日🎂\n再过' + str(differ_day) + '天就到了~\n', is_at_all=True)     # Text消息@所有人
        print(time.strftime("%Y-%m-%d") + name + '的生日提前提醒发送完毕~\n')
    elif differ_day==0 :
        name = bri_name
        xiaoding.send_text(msg='今天是【' + name + '】的生日🎂\n祝寿星生日快乐！\n', is_at_all=True)     # Text消息@所有人
        print(time.strftime("%Y-%m-%d") + name + '的当天生日提醒发送完毕~\n')

# bri_name = '吴承恩'
# bri_mon = 11
# bri_day = 1
# birthdayNotice_job(bri_name,bri_mon,bri_day)
