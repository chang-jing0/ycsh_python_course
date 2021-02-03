x = []

n = int(input('要排序幾個數 : '))

for i in range(n):
  y = int(input('請輸入第' + str(i+1) + '個數'))
  x.append(y)

x.sort()
x.reverse()

for j in range(n):
  print(x[j])