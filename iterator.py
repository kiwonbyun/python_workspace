msg = "반복 문장!"
count = 1
while count <= 5:
    count = count + 1
    print(msg)


sum = 0
n =1
last = int(input('언제까지 더할까요'))
while n <= last:
    sum = sum + n
    n = n+1

print(sum)

iter = 1
level = int(input('몇단을 출력할까요'))
while iter <= 9 :
    print(level, 'X', iter, '=', level * iter)
    iter = iter + 1
