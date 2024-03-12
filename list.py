import math

def 원뿔부피(r,h):
    return 1/3 * math.pi * r**2 * h
def 원뿔겉넓이(r,h):
    return (math.pi * r) * (r + h)


# hei_list = [1,3,7,14,22]
# for hei in hei_list :
#     print("원뿔 부피는",원뿔부피(10, hei))
#     print("원뿔 겉넓이는",원뿔겉넓이(10, hei))

for i in range(1,6):
    print('반복!!')


rad_list = range(10,40,10)
hei_list = [1,5,14]

for r,h in zip(rad_list, hei_list):
    print("원뿔 부피는",원뿔부피(r, h))
    print("원뿔 겉넓이는",원뿔겉넓이(r, h))