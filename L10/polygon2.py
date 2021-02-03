import math
def polygon(r,n):
  return r**2 * math.sin(math.pi*2/n) * n / 2

r = int(input('請輸入外接圓半徑 :'))
n = int(input('請輸入多邊形邊數 :'))

area = polygon(r,n)
print(area)