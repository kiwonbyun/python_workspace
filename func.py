def get_cone_vol_surf(r,h):
    if(r>0 and h>0):
        vol = 1/3 * 3.14 * (r**2) *h
        surf = 3.14 * r**2 + 3.14 * r * h
        return format(vol, '.2f'),format(surf, '.2f')
    else:
        print('반지름과 높이값에 양수를 입력하세요')


# prt_cone_vol(10,10)

# 입력받은 숫자를 역순으로 출력하는 함수
def prt_reverse_num():
    input_value = int(input('숫자를 입력하세요'))
    num = input_value
    while num != 0:
        digit = num % 10
        num = num // 10
        print(digit, end='')
vol1, surf1 = get_cone_vol_surf(10,20)
# print(vol1, surf1,'입니다.!')

# 동시할당!?
# temp = 17
# season = 'summer'
# === temp, season = 17,'summer' 동시할당 기능으로 swap이 쉬워진다.
# rad, hei = hei, rad

# a = int(input('첫번째 숫자를 입력하세요'))
# b = int(input('두번째 숫자를 입력하세요'))
# c = int(input('세번째 숫자를 입력하세요'))

def sortNum(num1, num2, num3):
    if(num1 > num2):
        num1, num2 = num2, num1
    if(num1 > num3):
        num1, num3 = num3, num1
    if(num2 > num3):
        num2, num3 = num3, num2
    
    return num1, num2, num3
        
# print(sortNum(a,b,c), '입니다')

def get_cone(r=10,h=10):
    if(r>0 and h>0):
        vol = 1/3 * 3.14 * (r**2) *h
        surf = 3.14 * r**2 + 3.14 * r * h
        return format(vol, '.2f'),format(surf, '.2f')
    else:
        print('반지름과 높이값에 양수를 입력하세요')

# print(get_cone())
# print(get_cone(10,10))

# 여러개의 수를 입력받고 합과 평균을 반환하는 함수
def var_sum_avg(*numbers):
    sum=0
    count=0
    for number in numbers:
        sum = sum + number
        count = count + 1
    return sum, sum/count

print(var_sum_avg(1,2,3,4,5,6,7,8,9,10))