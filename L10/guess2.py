import random

a = random.randint(1,100)

while True:
  x = int(input('請輸入猜的數字 :'))
  if x > a:
    print('猜大了')
   
  elif x < a:
    print('猜小了')

  else:
    print('猜中了')
    break 