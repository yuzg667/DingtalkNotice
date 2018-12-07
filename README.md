# DingtalkNotice
#### 介绍
这是一个python写的按照农历/阴历生日推送消息提醒的程序，当前使用的是钉钉消息推送。很好玩。

#### 环境：python3.6

#### 安装
1.下载源代码到本地

2.安装依赖包，命令：pip install requestments.txt

#### 快速使用-可进入钉钉群查看推送效果http://ww1.sinaimg.cn/large/7db06aably1fxx6ax9a4fj20ay0jrwfw.jpg
1.打开run.py修改“schedule.every().day.at("09:02").do(run)”自定义每天推送消息时间；
  
2.运行‘python run.py’  大功告成




#### 详细/自定义使用步骤：
1.进入birthday_notice.py 修改第16行access_token为你的access_token，access_token哪里来，参照https://open-doc.dingtalk.com/docs/doc.htm?treeId=257&articleId=105735&docType=1

2.打开data.csv添加寿星的农历/阴历生日列表：姓名,月,日。记住是农历的哦！！以英文逗号隔开，多个寿星换行。注意“月日”格式为“1”型，不是“01”型。

3.打开run.py

a.修改“for i in range(24)”中的数字为你的寿星个数(data.csv的行数)

b.修改“schedule.every().day.at("09:02").do(run)”自定义每天推送消息时间；

c.命中生日时间范围“birthdayNotice_job(bri_name,int(bri_mon),int(bri_day),futureDays=5)”中的futureDays字段。
  
4.运行‘python run.py’  大功告成
 
#### 其他
钉钉推送消息支持多样式，具体参考https://github.com/zhuifengshen/DingtalkChatbot 进行自定义你的样式
