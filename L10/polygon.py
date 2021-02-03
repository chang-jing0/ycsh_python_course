import math

r = int(input('請輸入外接圓半徑 :'))
n = int(input('請輸入多邊形邊數 :'))

area = r**2 * math.sin(math.pi*2/n) * n / 2
print(area)
