class IdentityError(Exception):
    def __str__(self):
        # return super().__str__()
        return '**본인인증 실패**'
    #Object(최상위 조상클래스가 물려준 메소드)
    #__str__ 재정의
    #다형성


    # def __init__(self, *args, **kwargs):
    #     self.__str__ = "에러발생"
    #     super().__init__(*args, **kwargs)
    # 실행안되는 코드

def transfer(name):
    if(name !='Yoseph'):
        #return -999 옛날식
        raise IdentityError()
        pass
    pass

#계좌이체 수행
try:
    transfer('been')
except(IdentityError) as e:
    print('- 계좌이체 실패 : 본인인증 실패')
    print('------------------------------------------------')
    
    print(e.__traceback__.tb_lineno)
    print(e.__traceback__.tb_frame)
    print(e.__traceback__.tb_lasti)
    print(e.__traceback__.tb_next)
    pass
finally:
    pass