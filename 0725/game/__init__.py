# 패키지 내 모듈을 미리 import 한다.
from .graphic.render import render_test

VERSION = 3.5

def print_version_info():
    print(f"The version oF this game is {VERSION}.")

#여기에 패키지 초기화 코드를 작성ㅎㄴ다.
print("Initializing game ...")