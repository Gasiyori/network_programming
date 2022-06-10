import smtplib
from email.message import EmailMessage
import filetype # 파일 유형을 판단해주는 모듈

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'ghdrldud99@gmail.com'
recipient = 'ghdrldud99@sch.ac.kr'
password = 'gfwoqwqqtmljuqfo'
# 수신자 목록
family = ['ghdrldud99@sch.ac.kr', 'ghdrldud99@gmail.com', 'ghdrldud99@naver.com']

msg = EmailMessage()
msg['Subject'] = '다중 메일 테스트'
msg['From'] = sender # 보내는 사람: sender's email address
msg['To'] = ', '.join(family) # 받는 사람: family 리스트에 있는 모든 email addresses
msg.set_content('내용을 입력하세요.')
msg.preamble = 'You will not see this in a MIME-aware mail reader.\n' # 첨부파일을 처리 못하는 경우, 출력

# 첨부할 파일 열기
with open('iot.png', 'rb') as f:
    img_data = f.read()

# add_attachment 함수를 이용해 파일 첨부. 파일 첨부시 첨부된 파일의 mime-type 지정
msg.add_attachment(img_data, maintype='image', subtype=filetype.guess_mime(img_data), filename='test.jpg')

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit()