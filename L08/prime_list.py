x = int(input('請輸入一個數當起點 \n'))
if x < 2:
  x = 2
y = int(input('請輸入一個數當終點 \n'))
for i in range(x,y+1):
  for j in range(2,i):
    if i % j == 0 and i != j:
      break
  else:
    print(i)
    


