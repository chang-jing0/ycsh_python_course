x = []
for i in range(3):
  y = int(input('請輸入第' + str(i+1) + '個數'))
  x.append(y)

x.sort()
x.reverse()
for j in range(3):
  print(x[j])
