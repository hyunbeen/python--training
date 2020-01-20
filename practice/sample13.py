import datetime
import time

#총 날짜 계산
print(datetime.timedelta(days=1, seconds=50, microseconds=0, milliseconds=12, minutes=0, hours=1, weeks=1))

#date 객체 날짜 표시
print(datetime.date(year=1, month=10, day=5))

#현재시간 표시
print(datetime.date.today())
print(datetime.date.fromtimestamp(time.time()))

#------------------------------------------------------------------------------


import smtplib

from email.mime.text import MIMEText


# 세션 생성
s = smtplib.SMTP('smtp.gmail.com', 587)


# TLS 보안 시작
s.starttls()


# 로그인 인증
s.login('lhbddong@gmail.com', 'fvflsbamnneymqjg')



# 보낼 메시지 설정
msg = MIMEText('내용 : 본문내용 테스트입니다.')
msg['Subject'] = '제목 : 메일 보내기 테스트입니다.'



# 메일 보내기
s.sendmail("lhbddong@gmail.com", "lhbddong@gmail.com", msg.as_string())


# 세션 종료
s.quit()

#----------------------------------------------------------------------

import urllib.request
import random
def download(URL):
    name = random.randrange(1,2001)
    fullName = str(name)+".jpg"
    urllib.request.urlretrieve(URL,fullName)

image_ddress = "http://imgnews.naver.com/image/5456/2017/12/12/0000002969_001_20171212105051175.jpg"
download(image_ddress)


#----------------------------------------------------------------------


