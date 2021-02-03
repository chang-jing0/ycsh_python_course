scores = [['John', 97],['Jack' ,83],['Jason',80],['Jimmy',77]]

i = scores[0] + scores[1] + scores[2] + scores[3]
print(i)

x = input('請輸入學生姓名 : ')
a = i.index(x)
if a != 0:
  print(i[a+1])
else:
  print('查無成績')