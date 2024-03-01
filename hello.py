import math
# print(1 / 3 * 3.14 * 20 ** 2 * 30 )
# print(3.14 * 20 ** 2 + 3.14 * 20 * 30)

rad = 20
height = 30

def 원뿔부피(r,h):
    return 1/3 * math.pi * r**2 * h

print(원뿔부피(rad,height))

def 원뿔겉넓이(r,h):
    return (math.pi * r) * (r + h)

print(원뿔겉넓이(rad,height))

# 정수 나눗셈
# print(5//2)

# print(25%7)

# print(8.4 % 0.9)

print(max(1,2,3,4))
print(min(1,2,3,4))
print(round(3.14))
