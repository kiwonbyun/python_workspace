import time

start_time = time.time()

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

prime_count = 0

for i in range(2,30000):
    if is_prime(i):
        prime_count = prime_count + 1

end_time = time.time()
print(end_time - start_time)
print("1~30000 사이에 소수는 총"+ str(prime_count) + '개 입니다.')