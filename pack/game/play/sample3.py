import sys



# sys.path.append('C:\\app\\py_workspace\\pack\\game\\graphic')
# print(sys.path)
# from render import *
# import os
# print(os.getcwd())
# render_test()
# python -m pack.game.play.sample3 스크립트 파일처럼 실행
print(__name__)
print(__package__)

from ..graphic.render import *

render_test()

