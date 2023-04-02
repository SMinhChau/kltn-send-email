from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from config import Config
from worker import worker
import smtplib


@worker.task(name='worker.send_mail', rate_limit='50/s')
def send(to_mail, message):
    mail = smtplib.SMTP_SSL(Config.SMTP_SERVER, Config.SMTP_PORT)
    mail.login(Config.EMAIL_USER, Config.PASSWORD)
    mime_html = MIMEText(message, 'html')

    message = MIMEMultipart("alternative")
    message["Subject"] = f'Thông báo khóa luận tốt nghiệp'
    message["From"] = formataddr(
        ('HT QL khóa luận tốt nghiệp', Config.EMAIL_SERVER))
    message["To"] = to_mail

    message.attach(mime_html)

    mail.sendmail(
        Config.EMAIL_SERVER,
        to_mail,
        message.as_string(),
    )
