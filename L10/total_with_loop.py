def total(n):
  m =0
  for i in range(1, n+1):
    m += i
  return m

n = int(input('請輸入一個正整數 :'))
t = total(n)
print(t)