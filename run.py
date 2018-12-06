# -*- coding: utf-8 -*-
 
from birthday_notice import birthdayNotice_job
import schedule
import time
def run():
    print("定时任务开始...")
    f_douhao = open(r"data.csv","r")
    line_douhao = f_douhao.readlines()
    for i in range(6):
        bri_name = (line_douhao[i].split(",")[0])
        bri_mon = (line_douhao[i].split(",")[1])
        bri_day = (line_douhao[i].split(",")[2])
        birthdayNotice_job(bri_name,int(bri_mon),int(bri_day),futureDays=5)
    f_douhao.close()

schedule.every().day.at("09:02").do(run)
while True:
    schedule.run_pending()
    time.sleep(1)
 
