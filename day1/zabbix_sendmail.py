#coding=utf-8
import smtplib
from email.mime.text import  MIMEText
import os
import argparse
import logging
import datetime

mail_host='smtp.sina.com'
mail_user='wangzhonghua84'
mail_Pass='58642891'
mail_postfix='sina.com'

def send_mail(mail_to,subject,content):
    me="zabbix监控告警平台"+"<"+mail_user+'@'+mail_postfix+">"
    msg=MIMEText(content)
    msg['Subject']=subject
    msg['From']=me
    msg['to']=mail_to
    global sendstatus
    global senderr

    try:
        smtp=smtplib.SMTP()
        smtp.connect(mail_host)
        smtp.login(mail_user,mail_Pass)
        smtp.sendmail(me,mail_to,msg.as_string())
        smtp.close()
        print('send ok')
        sendstatus=True
    except Exception as e:
        senderr=str(e)
        print(senderr)

def logwrite(sendstatus,mail_to,content):
    logpath='/etc/zabbix/alert'

    if not sendstatus:
        content = senderr

    if not os.path.isdir(logpath):
        os.makedirs(logpath)

    t=datetime.datetime.now()
    daytime=t.strftime('%Y-%m-%d')
    daylogfile=logpath+'/'+str(daytime)+'.log'
    logging.basicConfig(filename=daylogfile,level=logging.DEBUG)
    logging.info("*"*130)
    logging.debug(str(t)+'mail send to {0},content is :\n {1}'.format(mail_to,content))

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description='Send mail to user for zabbix alerting')
    parser.add_argument('mail_to',action="store",help='The address of the E-mail that send to user')
    parser.add_argument('subject',action="store",help='The subject of the E-mail')
    parser.add_argument('content',action='store',help='The content of the E-mail')
    args=parser.parse_args()
    mail_to=args.mail_to
    subject=args.subject
    content=args.content

    send_mail(mail_to,subject,content)
    logwrite(sendstatus,mail_to,content)