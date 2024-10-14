import smtplib
from email.mime.text import MIMEText
from email.header import Header



def send_email(to_email, title,content):
    # QQ邮箱服务器地址
    mail_host = 'smtp.qq.com'
    # QQ邮箱用户名
    mail_user = '2823558582@qq.com'
    # 授权码
    mail_pass = 'qtdrakxsasdbdeaj'
    # 发件人邮箱
    sender = '2823558582@qq.com'
    # 邮件主题
    subject = title
    # 实例化MIMEText邮件对象
    # message = MIMEText(content, 'plain', 'utf-8')
    message = MIMEText(content, 'html', 'utf-8')
    # 邮件主题
    message['Subject'] = Header(subject, 'utf-8')
    # 发件人
    message['From'] = sender
    # 收件人
    message['To'] = to_email

    try:
        # 连接邮件服务器
        server = smtplib.SMTP_SSL(mail_host, 465)
        # 登录服务器
        server.login(mail_user, mail_pass)
        # 发送邮件
        server.sendmail(sender, to_email, message.as_string())
        # 关闭连接
        server.quit()
        return 1
    except Exception as e:
        return 0

if __name__ == '__main__':
    send_email('1781591279@qq.com','test','<a href="https://drissionpage.cn/ChromiumPage/get_ele_info/"> a</a>')