import cx_Oracle

#한글 지원 방법
import os
os.putenv('NLS_LANG', '.UTF8')

#연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
connection = cx_Oracle.connect('kko','kko','192.168.0.9/xe')

cursor = connection.cursor()

cursor.execute(
   """
   select co_id
   from company
   """
)

# cursor.execute(
#    """
#    select c_id
#    from company
#    where text = :texting
#    """,
#    texting = "테스트"
# )

for co_id in cursor:
   print("테스트 이름 리스트 : ",co_id[0])
 