import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import ssl

FROM_ADDRESS = 'naoki.4438.virtual@gmail.com'
MY_PASSWORD = 'virtualtest'
TO_ADDRESS = 'naoki.4438.work@gmail.com'
BCC = ''
SUBJECT = 'GmailのSMTPサーバ経由'
BODY = 'pythonでメール送信、プログラムの動作は正常ではありません。本文を入力する箇所を確認してください。'

def create_message(from_addr, to_addr, bcc_addrs, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    return msg


def send(from_addr, to_addrs, msg): #メール送信のためにアカウントに入る
    #context = ssl.create_default_context()
    smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10)
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()

def gms_unit_do(to_addr_fm, subject_fm, body_fm): #fmはfrom main programの意味,unit実行時に実施する関数
    to_addr = to_addr_fm
    subject = subject_fm
    body = body_fm
    msg = create_message(FROM_ADDRESS, to_addr, BCC, subject, body)
    send(FROM_ADDRESS, to_addr, msg)

if __name__ == '__main__': #このプログラム単体での試験運用時に実施される

    to_addr = TO_ADDRESS
    subject = SUBJECT

    print ('メール本文を入れてください')
    body = input()

    msg = create_message(FROM_ADDRESS, to_addr, BCC, subject, body)
    send(FROM_ADDRESS, to_addr, msg)
