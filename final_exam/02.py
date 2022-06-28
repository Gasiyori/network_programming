# 짬뽕.
# 원격 접속 / 명령 실행 / 압축 / 메일 전송 등 배운 내용들을 전체적으로 사용 

import getpass
import paramiko
import time
import smtplib
from email.message import EmailMessage
import zipfile
import os

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'ghdrldud99@gmail.com'
recipient = ['daeheekim@sch.ac.kr', 'ninanooo@gmail.com']
password = 'gfwoqwqqtmljuqfo'

BUFF_SIZE = 65535

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

user = 'net_pro'
pwd = 'iot123'

cli.connect('114.71.220.5', username=user, password=pwd)
channel = cli.invoke_shell() # 새로운 셸 세션(channel) 생성

filename = '20171520.zip' # 압축파일의 이름
dirname = '/home/net_pro/20171520' # 압축할 폴더
CMD = 'zip -r ' + filename + ' ' + dirname # 리눅스 압축 명령어

# 채널을 통해 명령어 전송
channel.send('mkdir 20171520\n')
time.sleep(0.5)
channel.send('cd 20171520\n')
time.sleep(0.5)
channel.send('echo iot > iot.txt\n')
time.sleep(0.5)
stdin, stdout, stderr = cli.exec_command(CMD)
time.sleep(0.5)

sftp = cli.open_sftp()
sftp.get(filename, filename)

sftp.close()
cli.close()

msg = EmailMessage()
msg['Subject'] = '네트워크 프로그래밍 기말고사'
msg['From'] = sender
msg.set_content('네트워크 프로그래밍 기말고사 답안 제출합니다.')
msg['To'] = ', '.join(recipient) # 받는 사람: family 리스트에 있는 모든 email addresses

# 압축파일 메일에 첨부
with open(filename, 'rb') as f:
    msg.add_attachment(f.read(), maintype='application', subtype='zip', filename='20171520.zip')

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit()