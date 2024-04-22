import sys

try:
    value = int(input('0~1000 사이의 정수를 입력해주세요'))

    if value < 0 or value >1000:
        print('0~1000 사이의 정수만 허용됩니다.')
        sys.exit()
except ValueError:
    print("정수를 입력해주세요")
    sys.exit()

firstNum = value//1000
value %= 1000
secondNum = value//100
value %=100
thirdNum = value//10
value %= 10
fourthNum = value


print("각 자릿수의 총 합은 " + str(firstNum+ secondNum+ thirdNum+ fourthNum) + "입니다")