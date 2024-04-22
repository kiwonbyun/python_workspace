def calcNum():
    try:
        # 사용자로부터 입력 받기
        value = int(input('0~1000 사이의 정수를 입력해주세요: '))
        
        # 입력 값 범위 검증
        if value < 0 or value > 1000:
            raise ValueError("입력 값은 0에서 1000 사이의 정수여야 합니다.")

    except ValueError as e:
        print("유효하지 않은 입력입니다:", e)
        return   # 함수 종료#

    # 각 자릿수의 합을 계산
    firstNum = value // 1000  # 천의 자리
    value %= 1000
    secondNum = value // 100  # 백의 자리
    value %= 100
    thirdNum = value // 10  # 십의 자리
    value %= 10
    fourthNum = value  # 일의 자리

    # 자릿수 합 출력
    sum_of_digits = firstNum + secondNum + thirdNum + fourthNum
    print("각 자릿수의 총 합은", sum_of_digits, "입니다.")

calcNum()