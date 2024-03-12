a = int(input('첫번째 숫자를 입력해주세요'))
b = int(input('두번째 숫자를 입력해주세요'))
c = int(input('세번째 숫자를 입력해주세요'))

if a > b :
    if a > c :
        print(a)
    else :
        print(c) 
else :
    if b > c :
        print(b)
    else :
        print(c)
    