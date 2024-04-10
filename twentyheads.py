import random

try:
    target_num = random.randint(1,1001)

    try_count_list = list(range(1,21))

    for try_count in try_count_list:
        print(str(try_count) + "번째 시도입니다!")
        guess_num = int(input('1~1000 까지의 숫자중에 하나를 입력해주세요'))
        if guess_num == target_num:
            print('축하합니다' + str(try_count) + "번째 시도만에 맞혔습니다.")
            break
        else:
            if guess_num > target_num:
                print(str(guess_num) +"보다 작은 숫자입니다")
            else:
                print(str(guess_num) +"보다 큰 숫자입니다.")
            continue
        
    print('모든 기회를 사용했습니다. 다음에 다시 도전하세요')
except ValueError:
    print('올바른 값을 입력해주세요')
