x = int(input('請輸入一個數 \n'))

for i in range(2,x):
  if x % i == 0:
    print('不是質數')
    break
else:
  if x==1:
    print('不是質數')
  else:
    print('是質數')