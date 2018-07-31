# encoding: utf-8
from email.mime.application import MIMEApplication

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .settings import FILES_STORE, SMTP_HOST, SMTP_USER, SMTP_PWD, SMTP_PORT, SMTP_SENDER, SMTP_TO_LIST

class EmailHelper(object):
    def __init__(self):
        self.smtp_host = SMTP_HOST      # 发送邮件的smtp服务器
        self.smtp_user = SMTP_USER      # 用于登录smtp服务器的用户名，也就是发送者的邮箱
        self.smtp_pwd = SMTP_PWD         # 授权码，和用户名user一起，用于登录smtp， 非邮箱密码
        self.smtp_port = SMTP_PORT          # smtp服务器SSL端口号，默认是465
        self.sender = SMTP_SENDER       # 发送方的邮箱
        self.toLst = SMTP_TO_LIST

    def sendEmailWithAttr(self, result, item):
        message = MIMEMultipart()
        message['From'] = self.sender               # 发件人
        message['To'] = ",".join(self.toLst)                 # 收件人列表
        message['Subject'] = item['topic_title']                # 邮件标题
        message.attach(MIMEText(item['topic_title'], 'plain', 'utf-8'))

        for downItem in result:
            if downItem[0] == True:
                filename = './' + FILES_STORE + '/' + downItem[1]['path']
                with open(filename, 'rb') as f:
                    attachfile = MIMEApplication(f.read())
                filename = downItem[1]['path'].split('/')[-1]
                attachfile.add_header('Content-Disposition', 'attachment', filename=filename)
                encoders.encode_base64(attachfile)
                message.attach(attachfile)

        try:
            smtpSSLClient = smtplib.SMTP(self.smtp_host, self.smtp_port)
            loginRes = smtpSSLClient.login(self.smtp_user, self.smtp_pwd)
            print(f"登录结果：loginRes = {loginRes}")
            if loginRes and loginRes[0] == 235:
                print(f"登录成功，code = {loginRes[0]}")
                smtpSSLClient.sendmail(self.sender, self.toLst, message.as_string())
                print(f"发送成功. message:{message.as_string()}")
            else:
                print(f"登陆失败，code = {loginRes[0]}")
        except Exception as e:
            print(f"发送失败，Exception: e={e}")

        # print("-----------------------发送成功-----------------------")
