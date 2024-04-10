import random

try:
    guess_str = input('1~45 숫자중 6개를 쉽표로 분리하여 입력하세요')
    guess_num = list(map(int,guess_str.split(',')))
    lotto_num = random.sample(range(1,46,1),6)

    if len(guess_num) != 6:
        print('6개의 숫자를 선택하세요!!!')
        exit()

    hit_count = 0

    for guess in guess_num:
        if guess in lotto_num:
            hit_count = hit_count + 1

    print("예상 숫자는" + str(guess_num) + '입니다.')
    print("당첨 숫자는" + str(lotto_num) + '입니다.')
    print(str(hit_count) + "개 맞혔습니다")
    
except ValueError:
    print("올바르게 입력해주세요")