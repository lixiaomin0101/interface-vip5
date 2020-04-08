
'''
1.导入email相关的包
2.配置邮件的基本属性（发送人，接收人，邮件标题，用户名，密码，邮件服务器）
    添加附件
3.创建邮件发送实例
4.连接邮件服务器
5.发送邮件
'''
from smtplib import SMTP

# 发送html内容的邮件
import smtplib,time,os
from  email.mime.text import MIMEText
from email.header import Header

def sendMail(content):
    # 第一步配置邮箱属性
    # 发送邮箱
    sender ='lixiaomin0163@163.com'
    # 接收邮箱
    receiver ='1291561747@qq.com'
    # 发送邮件的主题
    t=time.strftime("%Y%m%d %H%M%s",time.localtime())
    subject='自动化测试结果'+t
    # 发送邮箱服务器
    smtpsever ='smtp.163.com'

    # 发送邮箱用户名/密码
    username='lixiaomin0163'
    passwod='tiancan123.'
    content =content


    # 第二步组装邮件内容和标题，中文需要参数utf-8，单字字节不需要
    msg = MIMEText(content,'plain','utf-8')
    msg['Subject'] =Header(subject,'utf-8')
    msg['From'] =sender
    msg['To'] =receiver

    # 第三步登录并且发送邮件
    try:
        # 1-实例化smtp类
        se =smtplib.SMTP()
        # 2-连接stmp服务器
        se.connect(smtpsever)
        # 3-登录邮箱
        se.login(username,passwod)
        # 4-设置发件人，收件人，邮箱内容
        se.sendmail(sender,receiver,msg.as_string())
    except:
        print("邮件发送失败")
    else:
        print("邮件发送成功")
    finally:
        se.quit()
def readTxt():

    f = open("/Applications/work/untitled/interfaceTestVip5/report/testReport.html","r");
    data = f.readlines();
    f.close()
    return str(data)
# 测试邮件是否发送成功

content = readTxt()
sendMail(content)
# readTxt()