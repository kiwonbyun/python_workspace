level = range(1,10)
iter = range(1,10)

for lv in level :
    print(lv,'|', end='')
    for it in iter :
        print(format(lv * it, '>4d'), end='')
    print()