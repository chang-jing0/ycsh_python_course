x = int(input("輸入一個數字"))
y = int(input("輸入一個數字"))
while x>1:
  for i in range(2,min(x,y)+1):
    
    if x % i == 0 and y % i == 0:
      print(i)
      x = x // i
      y = y // i
      break