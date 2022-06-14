import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "smtp.qq.com"  # 设置服务器
mail_user = ""  # 用户名
mail_pass = ""  # 授权码，注意不是邮箱登录密码，是上述设置的授权密码！！！
sender = ''
receivers = ['']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
def sendEmail()
  message = MIMEText('test', 'plain', 'utf-8')
  message['From'] = ""
  message['To'] = ""
  subject = 'test email'
  message['Subject'] = Header(subject, 'utf-8')
  smtpObj = smtplib.SMTP()
  smtpObj.connect(mail_host, 25)
  smtpObj.set_debuglevel(1)
  smtpObj.login(mail_user, mail_pass)
  smtpObj.sendmail(sender, receivers, message.as_string())
  print("邮件发送成功")
