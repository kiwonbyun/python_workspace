# 삼각형 출력하기
import math

print('   *')
print('  ***')
print(' *****')
print('*******')

# 인풋으로 받은 데이터는 문자열로 입력된다.
rad = int(input("반지름의 값을 입력하세요:"))
height = int(input('원뿔의 높이를 입력하세요:'))

def 원뿔부피(r,h):
    return 1/3 * math.pi * r**2 * h
def 원뿔겉넓이(r,h):
    return (math.pi * r) * (r + h)

print("원뿔의 부피는:",원뿔부피(rad, height))
print("원뿔의 겉넓이는:",원뿔겉넓이(rad, height))